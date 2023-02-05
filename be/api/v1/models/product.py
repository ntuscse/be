from pydantic import BaseModel


class Product(BaseModel):
    id: str
    name: str
    price: int
    images: list[str]
    sizes: list[str]
    colorways: list[str]
    productCategory: str  # todo: change to productCat enum model
    currentQty: int
    isAvailable: bool = True
    # maxQty: int
