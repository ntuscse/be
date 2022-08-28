from pydantic import BaseModel
from typing import Optional


class CartItem(BaseModel):
    productId: str
    size: Optional[str]
    quantity: int
