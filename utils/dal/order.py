import os
from be.api.v1.models.orders import Order
from utils.aws.dynamodb import read_item_from_db, write_item_to_db

table_name = os.environ.get("ORDERS_TABLE_NAME", "test_orders_table")

def dal_create_order(order: Order):
    orderItems = [{
        "id": orderItem.id,
        "name": orderItem.name,
        "price": int(orderItem.price*100),
        "product_category": orderItem.productCategory,
        "image": orderItem.image,
        "quantity": orderItem.quantity,
        "colorway": orderItem.colorway,
        "size": orderItem.size,
    } for orderItem in order.orderItems]

    order_dict = {
        "orderID": order.orderID,
        "orderDateTime": order.orderDateTime.__str__(),
        "customerEmail": order.customerEmail,
        "transactionID": order.transactionID,
        "paymentGateway": order.paymentGateway,
        "status": order.status.value,
        "orderItems": orderItems,
    }


    write_item_to_db(table_name, order_dict)