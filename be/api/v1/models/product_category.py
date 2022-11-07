from pydantic import BaseModel


class ProductCategory(BaseModel):
    name: str