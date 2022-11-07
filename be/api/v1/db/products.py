from be.api.v1.endpoints.products.data import products


def read_product(product_id: str):
    if not product_id:
        raise Exception('no product_id was passed to getProduct db function')
    product = next((x for x in products if x.id == product_id), None)

    # todo: integrate dynamoDb products table, wrap with pydantic
    # product = read_item_from_db()

    return product

