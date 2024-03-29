from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import os
import stripe
from be.api.v1.templates.non_auth_route import create_non_auth_router

stripe.api_key = os.environ["STRIPE_SECRET_KEY"]

router = APIRouter(prefix="/payments/intent", tags=["checkout"])

class RequestBody(BaseModel):
    amount: int


@router.post("")
# Create a stripe payment intent
async def post_payment_intent(body: RequestBody):
    try:
        payment_intent = stripe.PaymentIntent.create(
            payment_method_types=["paynow"],
            payment_method_data={"type": "paynow"},
            amount=body.amount,
            currency="sgd"
        )

        return {
          "client_secret": payment_intent.client_secret
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

handler = create_non_auth_router(router)
