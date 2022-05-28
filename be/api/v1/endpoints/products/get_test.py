from utils.test_app import createTestClient
from be.api.v1.endpoints.products.get import router

client = createTestClient(router)


def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == {
        "products": [
            {"id": "1", "name": "Product 1"},
            {"id": "2", "name": "Product 2"},
            {"id": "3", "name": "Product 3"},
        ]
    }


def test_get_product():
    response = client.get("/products/2")
    assert response.status_code == 200
    assert response.json() == {"id": "2", "name": "Product 2"}
