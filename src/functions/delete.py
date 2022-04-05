import http.client as httplib

from pynamodb.exceptions import DoesNotExist, DeleteError
from src.models import CompareYourselfModel


def handler(event, context):
    print('event: {}'.format(event))
    user_id = 'b80199e5-b445-11ec-9fa4-61a43020f107' # 仮

    try:
        model = CompareYourselfModel.get(hash_key=user_id)
    except DoesNotExist:
        return {'statusCode': httplib.NOT_FOUND,
                'body': 'CompareYoreself {} not found'.format(user_id)}

    try:
        model.delete()
    except DeleteError:
        return {'statusCode': httplib.BAD_REQUEST,
                'body': 'Unable to delete CompareYoreself {}'.format(user_id)}

    return {'statusCode': httplib.NO_CONTENT}
