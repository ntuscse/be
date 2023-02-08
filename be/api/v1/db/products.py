from be.api.v1.models.product import Product
from utils.dal.products import dal_read_product


def read_product(product_id: str) -> Product:
    if not product_id:
        raise Exception('no product_id was passed to getProduct db function')

    product = dal_read_product(product_id)

    return product

