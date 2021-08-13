def update():
    dynamodb = boto3.resource('dynamodb', aws_access_key_id=access_key, aws_secret_access_key=secret_key,
                              region_name='us-east-1')
    table = dynamodb.Table('Users')

    table.update_item(
        Key={
            'id': 2,
        },
        UpdateExpression="set firstname = :g",
        ExpressionAttributeValues={
            ':g': "Jane"
        },
        ReturnValues="UPDATED_NEW"
    )


update()
