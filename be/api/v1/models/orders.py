from be.api.v1.models.product import Product


class OrderItem(Product):
    quantity: int
