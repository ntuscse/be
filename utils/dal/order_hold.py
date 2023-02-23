import os
from be.api.v1.models.orders import Order
from utils.aws.dynamodb import write_item_to_db
from be.api.v1.models.order_hold_entry import OrderHoldEntry


table_name = os.environ["ORDER_HOLD_TABLE_NAME"]


def dal_create_order_hold_entry(orderHoldEntry: OrderHoldEntry):
    write_item_to_db(table_name, orderHoldEntry.dict())