from pydantic import BaseModel
from typing import Optional

class CartItem(BaseModel):
    productId: str
    size: str
    quantity: int
    colorway: str
    
class Cart(BaseModel):
    items: list[CartItem]
    promoCode: Optional[str]

class PriceModel(BaseModel):
    currency: str
    subtotal: float
    discount: float
    grandTotal: float
