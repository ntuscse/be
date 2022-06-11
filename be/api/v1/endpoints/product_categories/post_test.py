from moto import mock_dynamodb
import pytest
from utils.test_app import createTestClient
from be.api.v1.endpoints.product_categories.post import router
from be.api.v1.endpoints.product_categories.test_utils import get_mock_db_item

client = createTestClient(router)

@pytest.mark.usefixtures("provision_mock_db")
@mock_dynamodb
def test_post_product_categories():
    req_body = {
        "name": "test-category"
    }
    response = client.post('/product-categories', json=req_body)
    item = get_mock_db_item()
    print(item)
    assert response.status_code == 200
    assert response.json() == {
        "status": "Product category successfully created",
        "category": "test-category"
    }