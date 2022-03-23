def get(type: str) -> dict:
    if (type == 'all'):
        return {'statusCode': 200, 'body': 'All data is here!'}
    elif (type == 'single'):
        return {'statusCode': 200, 'body': 'The single user data is here!'}
    else:
        return {'statusCode': 200, 'body': 'Hello from lambda'}


def handler(event, context):
    return get(type=event['pathParameters']['type'])
