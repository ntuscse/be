from pydantic import BaseModel
from datetime import datetime
from typing import List

class ReservedProduct(BaseModel):
    productID: str
    qty: int


class OrderHoldEntry(BaseModel):
    transactionID: str
    expiry: int
    reservedProducts: List[ReservedProduct]
