import pytest
from be.api.v1.endpoints.product_categories.test_utils import (
    create_mock_db_with_items,
    delete_mock_table,
)


@pytest.fixture(scope="package")
def provision_mock_db():
    print("Provisioning mock db")
    create_mock_db_with_items()
    yield
    print("deleting mock db")
    delete_mock_table()
