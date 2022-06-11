from moto import mock_dynamodb
from utils.test_app import createTestClient
from be.api.v1.endpoints.product_categories.get import router
from be.api.v1.endpoints.product_categories.test_utils import get_mock_db_item, create_mock_db_with_items, delete_mock_table

client = createTestClient(router)

@mock_dynamodb
def test_get_product_categories():
    create_mock_db_with_items()
    response = client.get('/product-categories/test_category')
    item = get_mock_db_item()
    assert response.status_code == 200
    assert response.json() == {'product_category': {'name': 'test_category'}}
