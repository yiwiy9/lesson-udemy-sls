def delete() -> dict:
    return {'statusCode': 200, 'body': 'Deleted!'}


def handler(event, context):
    return delete()
