from be.api.v1.templates.non_auth_route import create_non_auth_router
from utils.aws.dynamodb import read_db
from fastapi import APIRouter, HTTPException
import os

router = APIRouter(prefix="/product-categories")

@router.get("/{product_category_name}")
# Get specific product category
def get_product_category(product_category_name: str):
    try:
        key = {
            'name': {
                'S': product_category_name
            }
        }
        table_name = os.environ["PRODUCT_CATEGORIES_TABLE_NAME"]
        response = read_db(table_name, key)
        if not response:
            raise HTTPException(status_code=404, detail="Product category not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=e)

    return {'product_category': {'name': response['name']['S']}}


handler = create_non_auth_router(router)