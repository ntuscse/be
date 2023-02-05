from datetime import datetime
import os
from be.api.v1.models.orders import Order, OrderItem, OrderStatus
from utils.aws.dynamodb import read_item_from_db, write_item_to_db

table_name = os.environ.get("ORDERS_TABLE_NAME", "test_orders_table")

def dal_create_order(order: Order):
    items = [{
        "id": orderItem.id,
        "name": orderItem.name,
        "price": orderItem.price,
        "product_category": orderItem.productCategory,
        "image": orderItem.image,
        "quantity": orderItem.quantity,
        "colorway": orderItem.colorway,
        "size": orderItem.size,
    } for orderItem in order.items]

    order_dict = {
        "id": order.id,
        "dateTime": order.dateTime.__str__(),
        "customerEmail": order.customerEmail,
        "transactionID": order.transactionID,
        "paymentGateway": order.paymentGateway,
        "status": order.status.value,
        "items": items,
    }


    write_item_to_db(table_name, order_dict)

def dal_read_order(order_id: str) -> Order:
    key = {"id": order_id}

    res = read_item_from_db(table_name, key)

    if res is None:
        raise Exception("Order not found in db")

    items = [
        OrderItem(
            id=item["id"],
            name=item["name"],
            price=item["price"],
            productCategory=item["product_category"],
            image=item["image"],
            quantity=item["quantity"],
            colorway=item["colorway"],
            size=item["size"],
        ) for item in res["items"]
    ]

    return Order(
        id=res["id"],
        dateTime=datetime.fromisoformat(res["dateTime"]),
        customerEmail=res["customerEmail"],
        transactionID=res["transactionID"],
        paymentGateway=res["paymentGateway"],
        status=OrderStatus(res["status"]),
        items=items,
    )
