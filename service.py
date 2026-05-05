import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('tasks')

def create_task(task):
    item = {
        'id': str(uuid.uuid4()),
        'task': task,
        'status': 'pending',
        'createdAt': datetime.utcnow().isoformat()
    }

    table.put_item(Item=item)
    return item


def get_tasks():
    res = table.scan()
    return res.get('Items', [])


def delete_task(task_id):
    table.delete_item(Key={'id': task_id})
