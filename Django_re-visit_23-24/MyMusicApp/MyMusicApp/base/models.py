from django.core.validators import MinValueValidator
from django.db import models

from MyMusicApp.base.validators.minlenvaluevalidator import minlenvaluevalidator


# Create your models here.


class Profile(models.Model):
    MAX_USERNAME_LENGTH = 15
    MIN_USERNAME_LENGTH = 2

    username = models.CharField(
        max_length=15,
        validators=[minlenvaluevalidator, ],
    )

    email = models.EmailField()

    age = models.IntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(0), ],
    )

    def __str__(self):
        return self.username


class Album(models.Model):
    MAX_LENGTH = 30
    POP_MUSIC = 'Pop Music'
    JAZZ_MUSIC = 'Jazz Music'
    RnB_MUSIC = 'R&B Music'
    ROCK_MUSIC = 'Rock Music'
    HIP_HOP_MUSIC = 'Hip Hop Music'
    COUNTRY_MUSIC = 'Country Music'
    DANCE_MUSIC = 'Dance Music'
    OTHER = 'Other'

    YOUR_CHOICES = [
        (POP_MUSIC, 'Pop Music'),
        (JAZZ_MUSIC, 'Jazz Music'),
        (RnB_MUSIC, 'R&B Music'),
        (ROCK_MUSIC, 'Rock Music'),
        (HIP_HOP_MUSIC, 'Hip Hop Music'),
        (COUNTRY_MUSIC, 'Country Music'),
        (DANCE_MUSIC, 'Dance Music'),
        (OTHER, 'Other'),
    ]

    album_name = models.CharField(
        max_length=MAX_LENGTH,
        unique=True,
    )

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=MAX_LENGTH,
        choices=
        YOUR_CHOICES,

    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField()

    price = models.FloatField(

    )
