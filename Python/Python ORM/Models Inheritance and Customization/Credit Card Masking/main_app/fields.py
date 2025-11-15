from django.core.exceptions import ValidationError
from django.db import models

class MaskedCreditCardField(models.CharField):

    def get_prep_value(self, value):
        return "****-****-****-"+value[12:]

    def to_python(self, value):
        if value is None or len(value) == 0:
            return None
        if isinstance(value, str):
            return value
        return str(value)

    def from_db_value(self, value, expression, connection):
        if value is None or len(value) == 0:
            return None
        return value

    def validate(self, value, model_instance):

        if not isinstance(value, str):
            raise ValidationError("The card number must be a string")
        if not value.isnumeric():
            raise ValidationError("The card number must contain only digits")
        if len(value) != 16:
            raise ValidationError("The card number must be exactly 16 characters long")

        return value
