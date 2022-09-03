from utils.test_app import createTestClient
from be.api.v1.endpoints.cart.checkout.post import router

client = createTestClient(router)


def test_post_cart_checkout():
    req_body = {
        "items": [
            {
                "productId": 1,
                "quantity": 1
            }
        ]
    }
    response = client.post("/cart/checkout", json=req_body)
    assert response.status_code == 200
    assert response.json()['items'] == [{
            'id': '1',
            'name': 'Oversized Crew Neck Short Sleeve T-Shirt',
            'price': 22.9,
            'images': [
                'https://image.uniqlo.com/UQ/ST3/sg/imagesgoods/451406/item/sggoods_09_451406.jpg?width=1008&impolicy=quality_75'],
            'sizes': ['xs', 's', 'm', 'l'],
            'productCategory': 't-shirt',
            'isAvailable': True, 'quantity': 1
        }]
    assert response.json()['price'] =={'currency': 'sgd', 'discount': 0, 'grandTotal': 22, 'subtotal': 22}
    assert response.json()['payment']['paymentGateway'] == 'stripe'
    assert type(response.json()['payment']['clientSecret']) is str