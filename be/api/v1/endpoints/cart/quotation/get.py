from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from be.api.v1.models.cart import PriceModel, Cart
from be.api.v1.models.orders import OrderItem
from be.api.v1.utils.cart_utils import calc_cart_value, generate_order_items_from_cart
from be.api.v1.templates.non_auth_route import create_non_auth_router


router = APIRouter(prefix="/cart/quotation", tags=["cart"])

class GetQuotationResponseModel(BaseModel):
    items: list[OrderItem]
    price: PriceModel

@router.get("", response_model=GetQuotationResponseModel)
async def post_cart_checkout(cart: Cart):
    try:
        items_products = generate_order_items_from_cart(cart)

        price = calc_cart_value(items_products)

        return {
            "items": items_products,
            "price": price,
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

handler = create_non_auth_router(router)
