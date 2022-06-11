from moto import mock_dynamodb
from utils.test_app import createTestClient
from be.api.v1.endpoints.product_categories.post import router
from be.api.v1.endpoints.product_categories.test_utils import get_mock_db_item, create_mock_db, delete_mock_table

client = createTestClient(router)

@mock_dynamodb
def test_post_product_categories():
    req_body = {
        "name": "test-category"
    }
    response = client.post('/product-categories', json=req_body)
    item = get_mock_db_item()
    print(item)
    delete_mock_table()
    assert response.status_code == 200
    assert response.json() == {
        "status": "Product category successfully created",
        "category": "test-category"
    }