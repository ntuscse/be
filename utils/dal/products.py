import json
import boto3
import os
from fastapi import HTTPException
from be.api.v1.models.product import Product
from utils.aws.dynamodb import (
    read_item_from_db,
    write_item_to_db,
    read_all_items_from_db,
    update_item_in_db
)

table_name = os.environ["PRODUCTS_TABLE_NAME"]


def dal_all_read_products() -> list[Product]:
    res = read_all_items_from_db(table_name)
    products = []
    for product in res:
        product = json.loads(json.dumps(res, default=str))

        products.append(Product(
            id=product["id"],
            name=product["name"],
            price=product["price"],
            images=product["images"],
            sizes=product["sizes"],
            sizeChart=product["size_chart"],
            colorways=product["colorways"],
            productCategory=product["product_category"],
            stock=product["stock"],
            isAvailable=product["is_available"],
        ))

    return products


def dal_read_product(item_id: str) -> Product:
    print("ATTEMPTING TO dal_read_product")
    key = {"id": item_id}

    res = read_item_from_db(table_name, key)

    if res is None:
        raise Exception("No product found in db")

    res = json.loads(json.dumps(res, default=str))

    return Product(
        id=res["id"],
        name=res["name"],
        price=res["price"],
        images=res["images"],
        sizes=res["sizes"],
        colorways=res["colorways"],
        stock=res["stock"],
        productCategory=res["product_category"],
        isAvailable=res["is_available"],
    )

def dal_increment_stock_count(item_id: str, increment_value: int, size: str, color: str):
    key = {"id": item_id}
    update_expression = f'ADD stock.#color.#size :incrementValue'
    condition_expression = 'is_available = :isAvailable AND stock.#color.#size >= :incrementValue'
    expression_attribute_values = {
        ':incrementValue': increment_value,
        ':isAvailable': True,
    }
    expression_attribute_names = {
        '#color': color,
        '#size': size
    }
    update_item_in_db(table_name, key, update_expression, condition_expression, expression_attribute_values, expression_attribute_names)

def dal_create_product(product: Product):
    product_dict = {
        "id": product.id,
        "name": product.name,
        "price": product.price,
        "images": product.images,
        "sizes": product.sizes,
        "size_chart": product.sizeChart,
        "colorways": product.colorways,
        "product_category": product.productCategory,
        "stock": product.stock,
        "is_available": product.isAvailable,
    }
    write_item_to_db(table_name, product_dict)
