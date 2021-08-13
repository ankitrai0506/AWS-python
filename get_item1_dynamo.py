def get_item():
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                              region_name='us-east-1')
    table = dynamodb.Table('Users')
    resp = table.get_item(
        Key={
            'id': 2,
        }
    )

    if 'Item' in resp:
        print(resp['Item'])

get_item()
