from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User

from django.db import models

from petstagram.accounts.managers import PetstagramUserManager

# Create your models here.
'''
1. Create the models
2. Configure this model in settings.py
3. Create the user-manager
'''


class PetstagramUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LEN = 25

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        unique=True
    )

    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    objects = PetstagramUserManager()

# UserProfile = get_user_profile()