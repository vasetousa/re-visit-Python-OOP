from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator, MinLengthValidator, MinValueValidator
from django.db import models

GENRES_CHOICES = (
    ("Pop Music", "Pop Music"),
    ("Jazz Music", "Jazz Music"),
    ("R&B Music", "R&B Music"),
    ("Rock Music", "Rock Music"),
    ("Country Music", "Country Music"),
    ("Dance Music", "Dance Music"),
    ("Hip Hop Music", "Hip Hop Music"),
    ("Other", "Other"),
)


def characters_validator(value):
    for char in value:
        if not char.isdigit() and not char.isalpha() and not char == '_':
            raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")


class Profile(models.Model):
    username = models.CharField(max_length=15, validators=[MinLengthValidator(2), characters_validator])
    email = models.EmailField()
    age = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(2)])


class Album(models.Model):
    album_name = models.CharField(max_length=30, unique=True, validators=[characters_validator])
    artist = models.CharField(max_length=30)
    genre = models.CharField(max_length=20, choices=GENRES_CHOICES)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(verbose_name='Image URL:')  # a way to make a label
    price = models.FloatField(validators=[MinValueValidator(0)])
