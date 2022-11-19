import os
from be.api.v1.models.orders import Order
from utils.aws.dynamodb import read_item_from_db, write_item_to_db

table_name = os.environ["ORDERS_TABLE_NAME"]

def dal_create_order(order: Order):
    orderItems = [{
        "id": orderItem.id,
        "name": orderItem.name,
        "price": int(orderItem.price*100),
        "images": orderItem.images,
        "sizes": orderItem.sizes,
        "product_category": orderItem.productCategory,
        "quantity": orderItem.quantity,
        "size": orderItem.size,
    } for orderItem in order.orderItems]

    item = {
        "orderID": order.orderID,
        "orderDateTime": order.orderDateTime.__str__(),
        "customerEmail": order.customerEmail,
        "transactionID": order.transactionID,
        "paymentGateway": order.paymentGateway,
        "status": order.status.value,
        "orderItems": orderItems
    }


    write_item_to_db(table_name, item)

    print(read_item_from_db(table_name, {"orderID": order.orderID}))