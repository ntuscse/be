from moto import mock_dynamodb
import pytest
from utils.test_app import createTestClient
from be.api.v1.endpoints.product_categories.delete import router
from be.api.v1.endpoints.product_categories.test_utils import get_mock_db_item


@mock_dynamodb
@pytest.mark.usefixtures("provision_mock_db")
def test_delete_product_categories():
    client = createTestClient(router)
    response = client.delete('/product-categories/test-category')
    item = get_mock_db_item()
    assert response.status_code == 200
    assert response.json() == {
        'status': 'Product category successfully deleted',
        'category': 'test-category'
    }
    assert item is None
