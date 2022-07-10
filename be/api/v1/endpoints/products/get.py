from fastapi import APIRouter
from be.api.v1.templates.non_auth_route import create_non_auth_router


router = APIRouter(prefix="/products")


@router.get("")
# gets all products
async def get_products():
    return {
        "products": [
            {"id": "1", "name": "Product 1"},
            {"id": "2", "name": "Product 2"},
            {"id": "3", "name": "Product 3"},
        ]
    }


@router.get("/{item_id}")
# gets a single product
async def get_a_product(item_id):
    return {"id": item_id, "name": "Product " + item_id}


handler = create_non_auth_router(router)
