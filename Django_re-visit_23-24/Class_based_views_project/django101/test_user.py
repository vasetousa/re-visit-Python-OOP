from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

UserModel = get_user_model()
UserModel.objects.create_user(
    username="Pesho123",
    password='1234',
    first_name="Pesho",
    last_name="Goshov",
)

