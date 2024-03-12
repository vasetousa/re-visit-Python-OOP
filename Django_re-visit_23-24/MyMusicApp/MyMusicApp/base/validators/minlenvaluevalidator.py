from django.core.exceptions import ValidationError


def minlenvaluevalidator(value):
    if len(value) < 2:
        raise ValidationError("Username is too short")
