from pydantic import BaseModel
from typing import Optional

class OrderItem(BaseModel):
    id: str
    name: str
    price: int
    productCategory: str  # todo: change to productCat enum model
    quantity: int
    image: str
    colorway: str
    size: Optional[str]
