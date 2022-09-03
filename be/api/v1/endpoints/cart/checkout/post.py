from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import stripe
from be.api.v1.templates.non_auth_route import create_non_auth_router
from be.api.v1.models.cart import PriceModel, Cart
from be.api.v1.models.orders import OrderItem
from be.api.v1.utils.cart_utils import calc_cart_value, generate_order_items_from_cart

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

router = APIRouter(prefix="/cart/checkout", tags=["cart"])

class PaymentModel(BaseModel):
    paymentGateway: str
    clientSecret: str

class PostCheckoutResponseModel(BaseModel):
    items: list[OrderItem]
    price: PriceModel
    payment: PaymentModel


@router.post("", response_model=PostCheckoutResponseModel)
# Create an order with status payment-processing
async def post_checkout(cart: Cart):
    try:
        # calculate subtotal
        items_products = generate_order_items_from_cart(cart)

        price = calc_cart_value(items_products)

        payment_intent = stripe.PaymentIntent.create(
            payment_method_types=["paynow"],
            payment_method_data={"type": "paynow"},
            amount=int(price.grandTotal * 100), # stripe payment amounts are in cents
            currency="sgd"
        )

        return {
            "items": items_products,
            "price": price,
            "payment": {
                "paymentGateway": 'stripe',
                "clientSecret": payment_intent.client_secret
            }
        }


    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


handler = create_non_auth_router(router)
