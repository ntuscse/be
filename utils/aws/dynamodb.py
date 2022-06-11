import boto3
import os
from botocore.config import Config
from dotenv import load_dotenv

load_dotenv()

dynamodb = boto3.client(
    'dynamodb', 
    region_name='ap-southeast-1'
)

def read_db(table_name, key, pagination = False):
    response = dynamodb.get_item(
        TableName=table_name,
        Key=key
    )
    return response.get('Item')

def write_db(table_name, item):
    response = dynamodb.put_item(
        TableName=table_name,
        Item=item
    )
    waiter = dynamodb.get_waiter('table_exists')
    waiter.wait(TableName=table_name)
    print(response)
    return response

def update_db(table_name, item):
    response = dynamodb.update_item(
        TableName=table_name,
        Item=item
    )
    waiter = dynamodb.get_waiter('table_exists')
    waiter.wait(TableName=table_name)
    return response
  
def delete_db(table_name, key):
    response = dynamodb.delete_item(
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

def delete_table(table_name):
    dynamodb.delete_table(TableName=table_name)
    