import os
from utils.aws.dynamodb import (
    create_db,
    delete_table_from_db,
    write_item_to_db,
    read_item_from_db,
    dynamodb,
)


def create_mock_db():
    try:
        create_db(
            table_name=os.environ["PRODUCT_CATEGORIES_TABLE_NAME"],
            attribute_definitions=[{"AttributeName": "name", "AttributeType": "S"}],
            key_schema=[{"AttributeName": "name", "KeyType": "HASH"}],
            provisioned_throughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
    except dynamodb.exceptions.ResourceInUseException:
        return


def populate_db_with_items():
    items = ["category_to_be_deleted", "category_to_be_got"]
    for item in items:
        write_item_to_db(
            table_name=os.environ["PRODUCT_CATEGORIES_TABLE_NAME"],
            item={"name": {"S": item}},
        )


def get_mock_db_item(item):
    return read_item_from_db(
        table_name=os.environ["PRODUCT_CATEGORIES_TABLE_NAME"],
        key={"name": {"S": item}},
    )


def create_mock_db_with_items():
    create_mock_db()
    populate_db_with_items()


def delete_mock_table():
    delete_table_from_db(table_name=os.environ["PRODUCT_CATEGORIES_TABLE_NAME"])
