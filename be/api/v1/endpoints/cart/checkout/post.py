import os
import uuid
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime
import stripe
from be.api.v1.templates.non_auth_route import create_non_auth_router
from be.api.v1.models.cart import PriceModel, Cart
from be.api.v1.models.orders import OrderItem, Order, OrderStatus
from be.api.v1.utils.cart_utils import calc_cart_value, generate_order_items_from_cart
from utils.dal.order import dal_create_order

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

router = APIRouter(prefix="/cart/checkout", tags=["cart"])


class CheckoutRequestBodyModel(Cart):
    email: str


class PaymentModel(BaseModel):
    paymentGateway: str
    clientSecret: str


class PostCheckoutResponseModel(BaseModel):
    items: list[OrderItem]
    price: PriceModel
    payment: PaymentModel


@router.post("", response_model=PostCheckoutResponseModel)
# Create an order with status payment-processing
async def post_checkout(req: CheckoutRequestBodyModel):
    if not req.email:
        raise HTTPException(status_code=400, detail="Billing email must be provided when checking out")

    if not len(req.items):
        raise HTTPException(status_code=400, detail="Cart must not be empty when checking out")

    try:
        # calculate subtotal
        items_products = generate_order_items_from_cart(req)

        price = calc_cart_value(items_products)
        description = describe_cart(items_products)

        # todo: create "pending" order here - in db

        payment_intent = stripe.PaymentIntent.create(
            payment_method_types=["paynow"],
            payment_method_data={"type": "paynow"},
            amount=int(price.grandTotal),  # stripe payment amounts are in cents
            currency="sgd",
            receipt_email=req.email,
            description=f"SCSE Merch Purchase:\n{description}"
        )

        orderID = uuid.uuid4().__str__()
        orderDateTime = datetime.now().__str__()
        customerEmail = req.email
        transactionID = "payment_intent.id"
        paymentPlatform = "stripe"
        orderItems = items_products
        status = OrderStatus.PENDING_PAYMENT

        order = Order(
            orderID = orderID,
            orderDateTime = orderDateTime,
            customerEmail = customerEmail,
            transactionID = transactionID,
            paymentGateway = paymentPlatform,
            orderItems = orderItems,
            status = status
        )

        dal_create_order(order)

        return {
            "orderId": orderID,
            "items": items_products,
            "price": price,
            "payment": {
                "paymentGateway": "stripe",
                "clientSecret": payment_intent.client_secret
            },
            "email": req.email
        }


    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


handler = create_non_auth_router(router)
