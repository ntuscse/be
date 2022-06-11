import os
from utils.aws.dynamodb import create_db, delete_table, write_db, delete_table, read_db, dynamodb


def create_mock_db():
    try:
        create_db(
            table_name= os.environ["PRODUCT_CATEGORIES_TABLE_NAME"],
            attribute_definitions=[
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                }
            ],
            key_schema=[
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'
                }
            ],
            provisioned_throughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
    except dynamodb.exceptions.ResourceInUseException:
        return

def populate_db_with_items():
    write_db(
            table_name=os.environ["PRODUCT_CATEGORIES_TABLE_NAME"],
            item= {
            "name": {
                'S': 'test_category'
            }
        }
    )

def get_mock_db_item():
    return read_db(
        table_name=os.environ["PRODUCT_CATEGORIES_TABLE_NAME"],
        key={
            'name': {
                'S': 'test-category'
            }
        }
    )

def create_mock_db_with_items():
    create_mock_db()
    populate_db_with_items()

def delete_mock_table():
    delete_table(table_name=os.environ["PRODUCT_CATEGORIES_TABLE_NAME"])