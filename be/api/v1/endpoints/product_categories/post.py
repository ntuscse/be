from pydantic import BaseModel
from be.api.v1.templates.non_auth_route import create_non_auth_router
from utils.aws.dynamodb import write_db
from fastapi import APIRouter, HTTPException
import os


router = APIRouter(prefix="/product-categories")

class ProductCategory(BaseModel):
    name: str

@router.post("")
# Create an item in the product-categories table
async def create_product_category(product_category: ProductCategory):
    item = {
        "name": {
            'S': product_category.name
        }
    }
    table_name = os.environ["PRODUCT_CATEGORIES_TABLE_NAME"]
    write_db(table_name, item)
    return {
        "status": "Product category successfully created",
        "category": product_category.name,
    }

handler = create_non_auth_router(router)