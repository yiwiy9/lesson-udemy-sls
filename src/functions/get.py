import json
import http.client as httplib

from pynamodb.exceptions import DoesNotExist
from src.models import CompareYourselfModel


def handler(event, context):
    print('event: {}'.format(event))
    type = event['pathParameters']['type']

    if (type == 'all'):
        models = CompareYourselfModel.scan()
        return {'statusCode': httplib.OK,
                'body': json.dumps([dict(model) for model in models])}

    elif (type == 'single'):
        user_id = 'b80199e5-b445-11ec-9fa4-61a43020f107' # 仮

        try:
            model = CompareYourselfModel.get(hash_key=user_id)
        except DoesNotExist:
            return {'statusCode': httplib.NOT_FOUND,
                    'body': 'CompareYoreself {} not found'.format(user_id)}

        return {'statusCode': httplib.OK,
                'body': json.dumps([dict(model)])}

    else:
        return {'statusCode': httplib.BAD_REQUEST,
                'body': 'Invalid Path Parameter was given'}
