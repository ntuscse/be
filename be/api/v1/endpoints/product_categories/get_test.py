
import pytest
from utils.test_app import createTestClient
from be.api.v1.endpoints.product_categories.get import router
from be.api.v1.endpoints.product_categories.test_utils import get_mock_db_item

client = createTestClient(router)

def test_get_product_categories():
    response = client.get('/product-categories/test_category')
    assert response.status_code == 200
    assert response.json() == {'product_category': {'name': 'test_category'}}
