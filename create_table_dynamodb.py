import boto3
from boto3.dynamodb.conditions import Key

    access_key = ""
    secret_key = ""

def create_table():

    dynamodb = boto3.resource('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                              region_name='us-east-1')

    table = dynamodb.create_table(
        TableName='Users',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'N'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1,
        }
    )

    print("Table status:", table.table_status)

create_table()
