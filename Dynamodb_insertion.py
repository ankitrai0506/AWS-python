import boto3
from boto3.dynamodb.conditions import Key


def select_item(dbitem, table_name, primary_key, sort_key):
    access_key = ""
    secret_key = ""
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                              region_name='us-east-1')
    table = dynamodb.Table(table_name)

    update_expression = 'SET {}'.format(','.join(f'#{p}=:{p}' for p in dbitem))
    expression_attribute_values = {f':{p}': v for p, v in dbitem.items()}
    expression_attribute_names = {f'#{p}': p for p in dbitem}

    response = table.update_item(
        Key={
            primary_key: dbitem[primary_key],
            sort_key: dbitem[sort_key]
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=expression_attribute_values,
        ExpressionAttributeNames=expression_attribute_names
    )
    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        print(response)
    else:
        print("Not Found")

select_item('dbitem', 'table_name', 'primary_key', 'sort_key')
