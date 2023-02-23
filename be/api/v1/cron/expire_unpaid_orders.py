import boto3
from datetime import datetime
import os
from utils.aws.dynamodb import dynamodb
import sys


table_name = os.environ["ORDER_HOLD_TABLE_NAME"]

def handler(event, context):
    table = dynamodb.Table(table_name)

    # Get the current epoch time
    now = int(datetime.now().timestamp())

    # Scan the table to find all expired documents
    result = table.scan(
        FilterExpression="expiry < :now",
        ExpressionAttributeValues={":now": now}
    )

    # Delete the expired documents
    with table.batch_writer() as batch:
        for item in result["Items"]:
            batch.delete_item(Key={"transactionID": item["transactionID"]})

    return dict()