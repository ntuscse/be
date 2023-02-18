import os
from be.api.v1.models.product_category import ProductCategory
from utils.aws.dynamodb import (
    delete_item_from_db,
    read_item_from_db,
    write_item_to_db,
)


table_name = os.environ["PRODUCT_CATEGORIES_TABLE_NAME"]

def create_product_category(product_category_name: str):
    item = {
        {"name": {"S": product_category_name}}
    }
    write_item_to_db(table_name, item)

def get_product_category(product_category_name: str) -> ProductCategory:
    key = {
        {"name": {"S": product_category_name}}
    }
    res = read_item_from_db(table_name, key)

    return {
        "name": res["name"]["S"]
    }


def del_product_category(product_category_name: str) -> ProductCategory:
    key = {
        {"name": {"S": product_category_name}}
    }
    delete_item_from_db(table_name, key)
