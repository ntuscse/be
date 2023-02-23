import pytest
from utils.test_app import createTestClient
from be.api.v1.endpoints.cart.quotation.post import router

client = createTestClient(router)

@pytest.mark.skip(reason="test fails in ci, as setuo script doesnt create products table")
def test_post_cart_quotation():
    req_body = {
        "items": [
            {
                "productId": 1,
                "size": "s",
                "quantity": 1
            }
        ]
    }
    response = client.post("/cart/quotation", json=req_body)
    assert response.status_code == 200
    assert response.json() == {
        "items": [{
            "id": "1",
            "name": "Oversized Crew Neck Short Sleeve T-Shirt",
            "price": 22.9,
            "images": [
                "https://image.uniqlo.com/UQ/ST3/sg/imagesgoods/451406/item/sggoods_09_451406.jpg?width=1008&impolicy=quality_75"],
            "sizes": ["xs", "s", "m", "l"],
            "productCategory": "t-shirt",
            "size": "s",
            "isAvailable": True, "quantity": 1
        }],
        "price": {"currency": "sgd", "discount": 0.0, "grandTotal": 22.9, "subtotal": 22.9}
    }
