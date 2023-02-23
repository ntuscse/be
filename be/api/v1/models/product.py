from pydantic import BaseModel


class Product(BaseModel):
    id: str
    name: str
    price: int
    images: list[str]
    sizes: list[str]
    sizeChart: str
    colorways: list[str]
    productCategory: str  # todo: change to productCat enum model
    stock: dict[str, dict[str, int]]
    isAvailable: bool = True
