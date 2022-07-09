from fastapi import HTTPException
from pytest import raises
from be.api.v1.endpoints.products.get import products

from utils.test_app import createTestClient
from be.api.v1.endpoints.products.get import router

client = createTestClient(router)


def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == {'products': products}


def test_get_product_200():
    response = client.get("/products/2")
    assert response.status_code == 200
    assert response.json() == {"id": "2", "name": "Product 2"}

def test_get_product_404():
    with raises(HTTPException) as err:
        client.get("/products/999")
    assert err.value.status_code == 404
    assert err.value.detail == "Product not found"
