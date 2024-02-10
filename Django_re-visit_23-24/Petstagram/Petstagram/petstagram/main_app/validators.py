from functools import wraps

from django.core.exceptions import ValidationError


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError('Only letters are allowed')


def validate_file_max_size_in_mb(max_size):
    @wraps(validate_file_max_size_in_mb)
    def validate(value):
        filesize = value.file.size
        if filesize > max_size * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(max_size))

    return validate
