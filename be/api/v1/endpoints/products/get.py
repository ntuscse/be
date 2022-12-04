# import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from be.api.v1.templates.non_auth_route import create_non_auth_router
# from be.api.v1.endpoints.products.data import products
from be.api.v1.models.product import Product
from utils.dal.products import dal_read_products

router = APIRouter(prefix="/products", tags=["merchandise"])


class GetProductsResponseModel(BaseModel):
    products: list[Product]


@router.get("", response_model=GetProductsResponseModel)
# gets all products
async def get_products():
    # table_name = os.environ.get("PRODUCTS_TABLE_NAME")
    products_list = dal_read_products()
    print('products', products_list)

    return {"products": products_list}


@router.get("/{item_id}", response_model=Product)
# gets a single product
async def get_product(item_id: str):
    products_list = dal_read_products()
    for _index, item in enumerate(products_list):
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Product not found")


handler = create_non_auth_router(router)
