from fastapi import APIRouter, HTTPException
from be.api.v1.templates.non_auth_route import create_non_auth_router
from be.api.v1.models.orders import Order
from utils.dal.order import dal_read_order

router = APIRouter(prefix="/orders", tags=["merchandise"])

@router.get("/{order_id}", response_model=Order)
# gets a single order
async def get_order(order_id: str):
    try:
        return dal_read_order(order_id)
    except Exception as e:
        print("Error reading order:", e)
        raise HTTPException(status_code=404, detail="Order not found")


handler = create_non_auth_router(router)
