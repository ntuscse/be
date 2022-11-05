import pytest
from utils.test_app import createTestClient
from be.api.v1.endpoints.product_categories.get import router
from be.api.v1.endpoints.product_categories.test_utils import get_mock_db_item

client = createTestClient(router)


@pytest.mark.usefixtures("provision_mock_db")
@pytest.mark.skip(reason="test setup fails at create_mock_db()")
def test_get_product_categories_200():
    response = client.get("/product-categories/category_to_be_got")
    assert response.status_code == 200
    assert response.json() == {"product_category": {"name": "category_to_be_got"}}
