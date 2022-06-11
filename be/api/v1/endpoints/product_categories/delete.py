from ast import Str
from be.api.v1.templates.nonAuthRoute import createNonAuthRouter
from utils.aws.dynamodb import dynamodb
from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter(prefix="/product-categories")

@router.post("/{product_category_id}")
# Delete an item in the product-categories table
async def delete_product_category(category: Str):
    table = dynamodb.Table("product-categories")
    try:
        table.delete_item(
            Key={
                "name": category.name
            }
        )
    except Exception as e:
        raise Exception('Unable to delete a product category')
    return {
        "status": "Product category successfully deleted",
        "category": category
    }

handler = createNonAuthRouter(router)