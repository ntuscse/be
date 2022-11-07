from pydantic import BaseModel
from typing import Optional

class CartItem(BaseModel):
    productId: str
    size: Optional[str]
    quantity: int
class Cart(BaseModel):
    items: list[CartItem]
    promoCode: Optional[str]

class PriceModel(BaseModel):
    currency: str
    subtotal: float
    discount: float
    grandTotal: float
