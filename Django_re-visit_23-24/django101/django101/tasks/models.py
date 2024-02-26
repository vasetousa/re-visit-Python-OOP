from django.db import models


# Create your models here.

# Code-first approach
class Task(models.Model):
    title = models.CharField(
        max_length=15,
        null=False,
        # unique=True,
    )

    text = models.CharField(
        max_length=50,
    )

    def __str__(self):
        return f'{self.id}: {self.title}'


class Category(models.Model):
    name = models.CharField(
        max_length=20,
    )
