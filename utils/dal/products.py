import os
from be.api.v1.models.product import Product
from utils.aws.dynamodb import (
    delete_item_from_db,
    read_item_from_db,
    write_item_to_db, read_all_items_from_db
)

table_name = os.environ["PRODUCTS_TABLE_NAME"]

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


def dal_read_product(item_id: str) -> Product:
    print("ATTEMPTING TO dal_read_product")
    key = {"id": item_id}

    res = read_item_from_db(table_name, key)
    print(res)

    return Product(
        id=res["id"],
        name=res["name"],
        price=res["price"],
        images=res["images"],
        sizes=res["sizes"],
        colorways=res["colorways"],
        productCategory=res["product_category"],
        isAvailable=res["is_available"],
    )


def dal_delete_product_category(self, item_id: str) -> bool:
    key = {
        {"item_id": {"S": item_id}}
    }
    delete_item_from_db(table_name, key)
    return True
