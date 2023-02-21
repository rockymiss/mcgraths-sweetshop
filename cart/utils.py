from django.core.serializers.json import DjangoJSONEncoder
from decimal import Decimal


class CustomJSONEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return super().default(obj)