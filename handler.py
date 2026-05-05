import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tasks')

def lambda_handler(event, context):
    method = event.get('httpMethod')

    if method == 'POST':
        body = json.loads(event['body'])
        item = {
            'id': str(uuid.uuid4()),
            'task': body['task'],
            'status': 'pending',
            'createdAt': datetime.utcnow().isoformat()
        }
        table.put_item(Item=item)
        return response(200, item)

    elif method == 'GET':
        res = table.scan()
        return response(200, res['Items'])

    elif method == 'DELETE':
        id = event['queryStringParameters']['id']
        table.delete_item(Key={'id': id})
        return response(200, {"message": "deleted"})


def response(status, body):
    return {
        "statusCode": status,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }
