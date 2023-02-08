from moto import mock_dynamodb
import pytest
from fastapi import HTTPException
from pytest import raises

from utils.test_app import createTestClient
from be.api.v1.endpoints.product_categories.delete import router
from be.api.v1.endpoints.product_categories.test_utils import get_mock_db_item

client = createTestClient(router)


@pytest.mark.usefixtures("provision_mock_db")
@pytest.mark.skip(reason="test setup fails at create_mock_db()")
def test_delete_product_category_200():
    response = client.delete("/product-categories/category_to_be_deleted")
    item = get_mock_db_item("category_to_be_deleted")
    assert response.status_code == 200
    assert response.json() == {
        "status": "Product category successfully deleted",
        "category": "category_to_be_deleted",
    }
    assert item is None


@pytest.mark.skip(
    reason="deletion doesn't return if the item doesnt exist yet - to be added!"
)
@pytest.mark.usefixtures("provision_mock_db")
@pytest.mark.skip(reason="test setup fails at create_mock_db()")
def test_delete_product_category_404():
    with raises(HTTPException) as err:
        client.delete("/product-categories/category_that_doesnt_exist")
    item = get_mock_db_item("category_that_doesnt_exist")
    assert err.value.status_code == 404
    assert err.value.detail == "Product category does not exist"
    assert item is None
