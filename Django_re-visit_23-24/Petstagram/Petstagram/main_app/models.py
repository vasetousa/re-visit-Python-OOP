from django.db import models

# Create your models here.
import datetime

from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.main_app.validators import validate_only_letters, validate_file_max_size_in_mb


# Create your models here.
class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    MALE = 'Male'
    FEMALE = 'Female'
    NO_SHOW = 'Do not show'

    GENDERS = [(x, x) for x in (MALE, FEMALE, NO_SHOW)]
    MAX_LENGTH = max(len(c) for c in [MALE, FEMALE, NO_SHOW])

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True, blank=True,
    )
    # date_of_birth = forms.DateField(
    #     widget=SelectDateWidget()
    # )

    description = models.TextField(
        null=True, blank=True,
    )

    email = models.EmailField(
        null=True, blank=True,
    )

    gender = models.CharField(
        max_length=MAX_LENGTH,
        choices=GENDERS,
        null=True, blank=True,
        default=NO_SHOW,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    # Constants
    NAME_MAX_LENGTH = 30
    DOG = 'Dog'
    CAT = 'Cat'
    FISH = 'Fish'
    PARROT = 'Parrot'
    BUNNY = 'Bunny'
    OTHER = 'Other'

    MAX_LENGTH = max(len(c) for c in [DOG, CAT, FISH, PARROT, BUNNY, OTHER])
    TYPES = [(y, y) for y in (DOG, CAT, FISH, PARROT, BUNNY, OTHER)]

    # Fields(Columns)
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=MAX_LENGTH,
        choices=TYPES
    )

    date_of_birth = models.DateField(
        null=True, blank=True,
    )

    # Relations -> One to one, One to many, Many to Many
    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    @property
    def age(self):
        return datetime.datetime.now().year - self.date_of_birth.year

    class Meta:
        unique_together = ('user_profile', 'name')

    def __str__(self):
        return f'{self.name}'


class PetPhoto(models.Model):
    MAX_SIZE = 5

    # max photo size 5MB
    photo = models.ImageField(
        max_length=250,
        validators=(
            validate_file_max_size_in_mb(MAX_SIZE),
        )
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        # validate at least 1 pet
    )

    description = models.TextField(
        null=True, blank=True,
    )

    date_time_of_publication = models.DateTimeField(
        auto_now_add=True,
    )

    likes = models.IntegerField(
        default=0,
    )

    def __str__(self):
        return f'{self.photo}'
