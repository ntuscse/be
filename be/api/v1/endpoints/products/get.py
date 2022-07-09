import os
from fastapi import APIRouter, HTTPException
from be.api.v1.templates.non_auth_route import create_non_auth_router

router = APIRouter(prefix="/products")

products = [
    {"id": "1", "name": "Product 1"},
    {"id": "2", "name": "Product 2"},
    {"id": "3", "name": "Product 3"},
]


@router.get("", tags=["merchandise"])
# gets all products
async def get_products():
    table_name = os.environ.get("PRODUCTS_TABLE_NAME")
    return {'products': products}


@router.get("/{item_id}")
# gets a single product
async def get_product(item_id):
    for index, item in enumerate(products):
        if item['id'] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Product not found")


handler = create_non_auth_router(router)
