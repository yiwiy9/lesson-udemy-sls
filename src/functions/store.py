import json

def store(data: dict) -> dict:
    if 'age' not in data or not data['age']:
        return {'statusCode': 422, 'body': json.dumps({'error_message': 'Validation Failed'})}

    age = data['age']
    return {'statusCode': 200, 'body': json.dumps({'age': age * 2})}


def handler(event, context):
    print(event['body'])
    data = json.loads(event['body'])
    return store(data)
