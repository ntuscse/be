import os
from be.api.v1.models.product import Product
from utils.aws.dynamodb import (
    delete_item_from_db,
    read_item_from_db,
    write_item_to_db, read_all_items_from_db
)

table_name = os.environ["PRODUCTS_TABLE_NAME"]


def dal_create_product(self, product: Product):
    item = {
        {"id": {"S": product.id}},
        {"name": {"S": product.name}},
        {"price": {"N": product.price}},
        {"images": {"L": product.images}},
        {"sizes": {"L": product.sizes}},
        {"colorways": {"L": product.colorways}},
        {"product_category": {"S": product.productCategory}},
        {"is_available": {"B", product.isAvailable}},
    }
    write_item_to_db(table_name, item)


def dal_read_products() -> list[Product]:
    res = read_all_items_from_db(table_name)
    products = []
    for product in res:
        products.append(Product(
            id=product["id"],
            name=product["name"],
            price=product["price"],
            images=product["images"],
            sizes=product["sizes"],
            colorways=product["colorways"],
            productCategory=product["product_category"],
            isAvailable=product["is_available"],
        ))

    return products


def dal_read_product(self, item_id: str) -> Product:
    key = {
        {"name": {"S": item_id}}
    }
    res = read_item_from_db(table_name, key)

    return Product(
        id=res["item_id"]["S"],
        name=res["name"]["S"],
        price=res["name"]["N"],
        images=res["images"]["L"],
        sizes=res["images"]["S"],
        productCategory=res["product_category"]["S"],
        isAvailable=res["is_available"]["B"],
    )


def dal_delete_product_category(self, item_id: str) -> bool:
    key = {
        {"item_id": {"S": item_id}}
    }
    delete_item_from_db(table_name, key)
    return True
