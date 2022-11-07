from be.api.v1.models.product import Product
from typing import Optional

class OrderItem(Product):
    quantity: int
    size: Optional[str]
