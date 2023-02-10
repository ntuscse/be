from fastapi import APIRouter, HTTPException
from be.api.v1.templates.non_auth_route import create_non_auth_router
from be.api.v1.models.orders import Order
from utils.dal.order import dal_read_order

router = APIRouter(prefix="/orders", tags=["merchandise"])

@router.get("/{order_id}", response_model=Order)
# gets a single order
async def get_order(order_id: str):
    try:
        order = dal_read_order(order_id)
        # Censor the email associated with the order.
        split = order.customerEmail.split('@')
        username = split[0]
        if len(username) > 2:
            username = username[:2] + '*' * (len(username)-2)
        split[0] = username
        # order.customerEmail = split.join('@')
        order.customerEmail = '@'.join(split)
        return order
    except Exception as e:
        print("Error reading order:", e)
        raise HTTPException(status_code=404, detail="Order not found")


handler = create_non_auth_router(router)
