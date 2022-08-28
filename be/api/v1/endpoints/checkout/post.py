from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import os
import stripe
from be.api.v1.templates.non_auth_route import create_non_auth_router
from be.api.v1.models.cart import CartItem
from be.api.v1.models.orders import OrderItem
from be.api.v1.db.products import read_product

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

router = APIRouter(prefix="/checkout", tags=["checkout"])


class Cart(BaseModel):
    items: list[CartItem]
    promoCode: Optional[str]

class PriceModel(BaseModel):
    currency: str
    subtotal: int
    discount: int
    grandTotal: int

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
        items_products = []
        for i in cart.items:
            product = read_product(i.productId)
            if not product:
                raise HTTPException(status_code=400, detail=f"productId {i.productId} could not be found")
            items_products.append(
                OrderItem(
                    id=product.id,
                    name=product.name,
                    price=product.price,
                    images=product.images,
                    sizes=product.sizes,
                    productCategory=product.productCategory,
                    isAvailable=product.isAvailable,
                    quantity=i.quantity
                ))

        subtotal = 0
        for i in items_products:
            subtotal += i.price * i.quantity

        # handle promo code
        # promo = getPromo(promoCode) if cart.promoCode else None

        # discount_value = 0
        # if promo.target.type == 'cart':
        #     if promo.type == 'fixed_value':
        #         discount_value = promo.value
        #     elif promo.type == 'percentage':
        #         discount_value = promo.value * subtotal
        # if promo.target.type == 'product':
        #     discount_product_id = promo.target.product_id
        #     discount_product = next(item for item in items_products if item["productId"] == discount_product_id)
        #     if not discount_product:
        #         raise HTTPException(status_code=400, detail="Promo code can't be applied to any item in cart")
        #     if promo.type == 'fixed_value':
        #         item_discount_value = max(promo.value, discount_product.price)
        #
        #     elif promo.type == 'percentage':
        #         item_discount_value = promo.value * discount_product.price

        grand_total = subtotal

        payment_intent = stripe.PaymentIntent.create(
            payment_method_types=["paynow"],
            payment_method_data={"type": "paynow"},
            amount=int(grand_total * 100), # stripe payment amounts are in cents
            currency="sgd"
        )

        return {
            "items": items_products,
            "price": {
                "currency": 'sgd',
                "subtotal": subtotal,
                "discount": 0,
                "grandTotal": grand_total,
            },
            "payment": {
                "paymentGateway": 'stripe',
                "clientSecret": payment_intent.client_secret
            }
        }


    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


handler = create_non_auth_router(router)
