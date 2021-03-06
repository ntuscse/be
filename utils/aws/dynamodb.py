import boto3
import os
from botocore.config import Config
from dotenv import load_dotenv

load_dotenv()

is_offline = os.environ.get('IS_OFFLINE')

dynamodb_args = {
    'endpoint_url': 'http://localhost:8011',
    'aws_access_key_id': 'DEFAULT_ACCESS_KEY',
    'aws_secret_access_key': 'DEFAULT_SECRET',
    'verify': False
} if is_offline else {

}

dynamodb = boto3.client(
    'dynamodb',
    region_name='ap-southeast-1',
    **dynamodb_args
)


def read_item_from_db(table_name, key, pagination=False):
    response = dynamodb.get_item(
        TableName=table_name,
        Key=key
    )
    return response.get('Item')


def write_item_to_db(table_name, item):
    response = dynamodb.put_item(
        TableName=table_name,
        Item=item
    )
    waiter = dynamodb.get_waiter('table_exists')
    waiter.wait(TableName=table_name)
    return response


def update_item_in_db(table_name, item):
    response = dynamodb.update_item(
        TableName=table_name,
        Item=item
    )
    waiter = dynamodb.get_waiter('table_exists')
    waiter.wait(TableName=table_name)
    return response


def delete_item_from_db(table_name, key):
    response = dynamodb.delete_item(
        TableName=table_name,
        Key=key
    )
    waiter = dynamodb.get_waiter('table_exists')
    waiter.wait(TableName=table_name)
    return response


def create_db(table_name, attribute_definitions, key_schema, provisioned_throughput):
    table = dynamodb.create_table(
        TableName=table_name,
        AttributeDefinitions=attribute_definitions,
        KeySchema=key_schema,
        ProvisionedThroughput=provisioned_throughput
    )
    waiter = dynamodb.get_waiter('table_exists')
    waiter.wait(TableName=table_name)

    return table


def delete_table_from_db(table_name):
    dynamodb.delete_table(TableName=table_name)
