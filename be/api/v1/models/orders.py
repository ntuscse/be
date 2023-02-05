from pydantic import BaseModel
from typing import Optional
from enum import Enum
from datetime import datetime

class OrderStatus(Enum):
    PENDING_PAYMENT = 1
    PAYMENT_COMPLETED = 2
    ORDER_COMPLETED = 3

class OrderItem(BaseModel):
    id: str
    name: str
    price: int
    productCategory: str  # todo: change to productCat enum model
    image: str
    quantity: int
    colorway: str
    size: Optional[str]

class Order(BaseModel):
    id: str
    dateTime: datetime
    customerEmail: str
    transactionID: str
    paymentGateway: str
    items: list[OrderItem]
    status: OrderStatus
