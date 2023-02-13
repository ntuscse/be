from unittest.mock import patch
import pytest
from datetime import datetime
from utils.test_app import createTestClient
from be.api.v1.endpoints.orders.get import router

from be.api.v1.models.orders import Order, OrderStatus

client = createTestClient(router)

mock_order_data = Order(
    orderID="123",
    orderDateTime=datetime.fromisoformat("2023-02-10 10:26:43.387520"),
    customerEmail="test@example.com",
    transactionID="",
    paymentGateway="",
    orderItems=[],
    status=OrderStatus(1))

expected_api_res = {'customerEmail': 'te**@example.com',
                    'orderDateTime': '2023-02-10T10:26:43.387520',
                    'orderID': '123',
                    'orderItems': [],
                    'paymentGateway': '',
                    'status': 1,
                    'transactionID': ''}


def test_get_order():
    with patch("be.api.v1.endpoints.orders.get.dal_read_order", return_value=mock_order_data):
        response = client.get("/orders/123")
        assert response.status_code == 200
        print(response.json())
        assert response.json() == expected_api_res
