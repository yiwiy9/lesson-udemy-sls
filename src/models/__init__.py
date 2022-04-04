import os

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute


class CompareYourselfModel(Model):
    class Meta:
        table_name = os.environ['DYNAMODB_TABLE']
        region = os.environ['REGION']
        host = os.environ['DYNAMODB_HOST']

    user_id = UnicodeAttribute(hash_key=True, null=False)
    age = NumberAttribute(null=False)
    height = NumberAttribute(null=False)
    income = NumberAttribute(null=False)

    def __iter__(self):
        for name, attr in self.get_attributes().items():
            yield name, attr.serialize(getattr(self, name))
