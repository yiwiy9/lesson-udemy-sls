import json
import logging
import uuid
import http.client as httplib
from cerberus import Validator

from src.models import CompareYourselfModel


schema = {'age': {'type': 'integer'},
          'height': {'type': 'integer'},
          'income': {'type': 'integer'}}
v = Validator(schema=schema, require_all=True)

def handler(event, context):
    print('event: {}'.format(event))
    data = json.loads(event['body'])

    if (not v.validate(data)):
        logging.error(v.errors)
        return {'statusCode': httplib.UNPROCESSABLE_ENTITY,
                'body': json.dumps(v.errors)}

    new_model = store(data['age'], data['height'], data['income'])
    return {'statusCode': httplib.CREATED,
            'body': json.dumps(dict(new_model))}


def store(age: str, height: str, income: str) -> CompareYourselfModel:
    model = CompareYourselfModel(user_id=str(uuid.uuid1()),
                                     age=age,
                                     height=height,
                                     income=income)
    model.save()
    return model
