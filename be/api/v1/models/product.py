from pydantic import BaseModel
from typing import Dict


class Product(BaseModel):
    id: str
    name: str
    price: int
    images: list[str]
    sizes: list[str]
    colorways: list[str]
    productCategory: str  # todo: change to productCat enum model
    stock: Dict[str, Dict[str, int]]
    isAvailable: bool = True
