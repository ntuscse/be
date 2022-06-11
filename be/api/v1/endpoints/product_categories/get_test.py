from moto import mock_dynamodb
import pytest
from utils.test_app import createTestClient
from be.api.v1.endpoints.product_categories.get import router
from be.api.v1.endpoints.product_categories.test_utils import get_mock_db_item

client = createTestClient(router)

@pytest.mark.usefixtures("provision_mock_db")
@mock_dynamodb
def test_get_product_categories():
    response = client.get('/product-categories/test_category')
    assert response.status_code == 200
    assert response.json() == {'product_category': {'name': 'test_category'}}
