import os
from tkinter import E
from pydantic import BaseModel
from be.api.v1.models.product import Product
from utils.aws.dynamodb import (
    delete_item_from_db,
    read_item_from_db,
    write_item_to_db
)

table_name = os.environ["PRODUCT_TABLE_NAME"]

def create_product(self, product: Product):
    item = {
        {"id": {"S": product.id}},
        {"name": {"S": product.name}},
        {"price": {"N": product.price}},
        {"images": {"L": product.images}},
        {"sizes": {"L": product.sizes}},
        {"product_category": {"S": product.productCategory}},
        {"is_available": {"B", product.isAvailable}},
    }
    write_item_to_db(table_name, item)

def get_product(self, item_id: str) -> Product:
    key = {
        {"name": {"S": item_id}}
    }
    res = read_item_from_db(table_name, key)

    return {
        "item_id": res["item_id"]["S"],
        "name": res["name"]["S"],
        "price": res["name"]["N"],
        "images": res["images"]["L"],
        "sizes": res["images"]["S"],
        "product_category": res["product_category"]["S"],
        "is_available": res["is_available"]["B"],
    }


def del_product_category(self, item_id: str) -> Product:
    key = {
        {"item_id": {"S": item_id}}
    }
    delete_item_from_db(table_name, key)
