from be.api.v1.templates.nonAuthRoute import createNonAuthRouter
from fastapi import APIRouter


router = APIRouter(prefix="/products")


@router.get("")
# gets all products
async def root():
    return {"products": [
        {"id": "1", "name": "Product 1"},
        {"id": "2", "name": "Product 2"},
        {"id": "3", "name": "Product 3"},
    ]}


@router.get("/{item_id}")
# gets a single product
async def product(item_id):
    return {
        "id": item_id,
        "name": "Product " + item_id
    }


handler = createNonAuthRouter(router)
