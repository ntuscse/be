import os
import uuid
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
import stripe
from be.api.v1.templates.non_auth_route import create_non_auth_router
from be.api.v1.models.cart import PriceModel, Cart
from be.api.v1.models.order_hold_entry import OrderHoldEntry, ReservedProduct
from be.api.v1.models.orders import OrderItem, Order, OrderStatus
from be.api.v1.utils.cart_utils import calc_cart_value, describe_cart, generate_order_items_from_cart
from utils.dal.order import dal_create_order
from utils.dal.products import dal_increment_stock_count
from utils.dal.order_hold import dal_create_order_hold_entry

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]
DEFAULT_ORDER_EXPIRY_TIME = 1

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
    expiry: int


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
        transactionID = payment_intent.id
        paymentPlatform = "stripe"
        orderItems = items_products
        status = OrderStatus.PENDING_PAYMENT
        expiry = datetime.now() + timedelta(hours=int(os.environ.get("ORDER_EXPIRY_TIME", DEFAULT_ORDER_EXPIRY_TIME)))

        order = Order(
            orderID = orderID,
            orderDateTime = orderDateTime,
            customerEmail = customerEmail,
            transactionID = transactionID,
            paymentGateway = paymentPlatform,
            orderItems = orderItems,
            status = status
        )

        for orderItem in orderItems:
            dal_increment_stock_count(orderItem.id, -orderItem.quantity)

        reservedProducts = [ReservedProduct(productID=item.productId, qty=item.quantity) for item in req.items]
        orderHoldEntry = OrderHoldEntry(transactionID=transactionID, expiry=int(expiry.timestamp()), reservedProducts=reservedProducts)

        dal_create_order(order)
        dal_create_order_hold_entry(orderHoldEntry)

        return {
            "orderId": orderID,
            "items": items_products,
            "price": price,
            "payment": {
                "paymentGateway": "stripe",
                "clientSecret": payment_intent.client_secret
            },
            "email": req.email,
            "expiry": int(expiry.timestamp())
        }


    except Exception as e:
        raise HTTPException(status_code=500, detail=e)


handler = create_non_auth_router(router)
