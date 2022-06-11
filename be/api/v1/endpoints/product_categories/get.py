from be.api.v1.templates.nonAuthRoute import createNonAuthRouter
from utils.aws.dynamodb import read_db
from fastapi import APIRouter, HTTPException
import os

router = APIRouter(prefix="/product-categories")

@router.get("/{product_category_name}")
# Get specific product category
def get_product_category(product_category_name: str):
    key = {
        'name': {
            'S': product_category_name
        }
    }
    table_name = os.environ["PRODUCT_CATEGORIES_TABLE_NAME"]
    response = read_db(table_name, key)
    if not response:
        raise HTTPException(status_code=404, detail="Product category not found")

    return {'product_category': {'name': response['name']['S']}}


handler = createNonAuthRouter(router)