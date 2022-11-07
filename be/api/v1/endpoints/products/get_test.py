import pytest
from fastapi import HTTPException
from pytest import raises
from be.api.v1.endpoints.products.data import products
# todo: replace products dummy import eith db fixture
from utils.test_app import createTestClient
from be.api.v1.endpoints.products.get import router

client = createTestClient(router)

@pytest.mark.skip(reason="test fails in ci, as setuo script doesnt create products table")
def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    assert response.json() == {"products": []} # todo: replace [] eith db fixture


def test_get_product_200():
    response = client.get("/products/2")
    assert response.status_code == 200
    assert response.json() == products[1]


def test_get_product_404():
    with raises(HTTPException) as err:
        client.get("/products/999")
    assert err.value.status_code == 404
    assert err.value.detail == "Product not found"
