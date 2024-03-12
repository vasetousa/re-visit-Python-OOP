from django.core.exceptions import ValidationError


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Only letters are allowed')