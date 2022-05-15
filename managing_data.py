import boto3
import uuid
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def manage_put_item(data):
    #save item to DB
    try:
        logger.info('START - putting items to DynamoDB...')
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
            dynamodb.put_item(TableName='myDynamoDB', Item=obj['PutRequest']['Item'])
        return 0, "responce"
    except Exception:
        raise "hey exc"
