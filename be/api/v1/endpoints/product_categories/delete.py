import os
from be.api.v1.templates.non_auth_route import create_non_auth_router
from utils.aws.dynamodb import delete_db
from fastapi import APIRouter


router = APIRouter(prefix="/product-categories")

@router.delete("/{product_category_name}")
# Delete an item in the product-categories table
async def delete_product_category(product_category_name: str):
    table_name = os.environ["PRODUCT_CATEGORIES_TABLE_NAME"]
    key = {
        "name": {
            'S': product_category_name
        }
    }
    delete_db(table_name, key)
    return {
        "status": "Product category successfully deleted",
        "category": product_category_name
    }

handler = create_non_auth_router(router)