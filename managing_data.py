"""
Your module description
"""
import boto3
import uuid


def manage_put_item(data):
    # save item to DB
    try:
        dynamodb = boto3.client('dynamodb')
        items = {
            "RequestItems": {
                "myDynamoDB": []
            }
        }
        for item in data:
            item = {
                "PutRequest": {
                    "Item": {
                        "Id": {
                            "B": str(uuid.uuid4().hex)
                        },
                        "phone": {
                            "S": item.get('phone', '')
                        },
                        "email": {
                            "S": item.get('email', '')
                        },
                        "postal code": {
                            "S": item.get('postalcode', '')
                        }
                    }
                }
            }
            items['RequestItems']['myDynamoDB'].append(item)

        for obj in items['RequestItems']['myDynamoDB']:
            print(obj['PutRequest']['Item'])
            dynamodb.put_item(TableName='myDynamoDB', Item=obj['PutRequest']['Item'])
        return 0, "responce"
    except Exception:
        raise "hey exc"


def dynamodb_get_item():
    print("hello")
    dynamodb = boto3.client('dynamodb')
    print("he1")

    response = dynamodb.get_item(
        TableName='myDynamoDB',
        Key={
            'Id': {'N': '0'}
        }
    )
    print("he2")
    print(response['Item'])

    print("get all")
    table = dynamodb.Table('myDynamoDB')
    print("1")
    response = table.scan()

    print(response)
    data = response['Items']
    print(data)
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
