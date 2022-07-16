from pydantic import BaseModel


class Product(BaseModel):
    id: str
    name: str
    price: float
    images: list[str]
    sizes: list[str]
    productCategory: str  # todo: change to productCat enum model
    isAvailable: bool = True
    # maxQty: int
