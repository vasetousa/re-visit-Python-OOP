from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=200,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )
    completed = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-completed',)
