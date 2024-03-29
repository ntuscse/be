import boto3
import os
from dotenv import load_dotenv
from typing import Union


load_dotenv()

is_offline = os.environ.get('IS_OFFLINE')

dynamodb_args = {
    'endpoint_url': 'http://localhost:8011',
    'aws_access_key_id': 'DEFAULT_ACCESS_KEY',
    'aws_secret_access_key': 'DEFAULT_SECRET',
    'verify': False
} if is_offline else {

}

dynamodb = boto3.resource(
    'dynamodb',
    region_name='ap-southeast-1',
    **dynamodb_args
)

UpdateKey = dict[str, dict[str, Union[int,str]]]
ExpressionAttributeValues = dict[str, dict[str, Union[int,str]]]

######
# reference : https://dynobase.dev/dynamodb-python-with-boto3
#####

def read_item_from_db(table_name, key, pagination=False):
    table = dynamodb.Table(table_name)
    response = table.get_item(
        Key=key # Key is of format {<keyName>: <value>} eg {"orderID": order.orderID}
    )
    print("==== response from ddb =====")
    print(response)
    return response.get('Item')


def read_all_items_from_db(tableName, pagination=False):
    print("ATTEMPTING TO read_all_items_from_db")
    print(f"from tableName {tableName}")
    table = dynamodb.Table(tableName)
    response = table.scan()

    data = response['Items']

    print("=== start of table data ===")
    print(data)
    print("=== end of table data ===")

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    return data


def write_item_to_db(table_name, item):
    table = dynamodb.Table(table_name)
    response = table.put_item(
        Item=item
    )
    return response

def update_item_in_db(table_name: str, key: UpdateKey, update_expression: str = None, condition_expression: str = None, expression_attribute_values: dict = None, expression_attribute_names: dict = None):
    table = dynamodb.Table(table_name)
    response = table.update_item(
        Key=key,
        UpdateExpression=update_expression,
        ConditionExpression=condition_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ExpressionAttributeNames=expression_attribute_names,
    )
    return response

# TODO: Update based on https://dynobase.dev/dynamodb-python-with-boto3
def delete_item_from_db(table_name, key):
    response = dynamodb.delete_item(
        TableName=table_name,
        Key=key
    )
    waiter = dynamodb.get_waiter('table_exists')
    waiter.wait(TableName=table_name)
    return response

# TODO: Update based on https://dynobase.dev/dynamodb-python-with-boto3
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
