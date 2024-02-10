from django.db import models

# Create your models here.


""" This class is used to create MANY to ONE key dependency"""


class Department(models.Model):
    name = models.CharField(
        max_length=20,
        blank=False,
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    SOFT_DEV = 1
    HR = 2
    SECURITY = 3

    GOOGLE = 'Google'
    FACEBOOK = 'Facebook'
    LOCKHEED_MARTIN = 'Lockheed Martin'

    first_name = models.CharField(
        max_length=30,
        blank=False,
        null=False
    )

    last_name = models.CharField(
        max_length=40,
        blank=False,
        null=False,
        # default='No Name',
    )

    egn = models.CharField(
        max_length=10,
        verbose_name='EGN',
        default='**********'
    )

    email = models.EmailField()

    job_title = models.IntegerField(
        choices=(
            (SOFT_DEV, 'Software Engineering'),
            (HR, 'HR'),
            (SECURITY, 'Security')
        )
    )

    company = models.CharField(
        max_length=max(len(c) for c in [GOOGLE, FACEBOOK, LOCKHEED_MARTIN]),
        choices=(
            (GOOGLE, GOOGLE),
            (FACEBOOK, FACEBOOK),
            (LOCKHEED_MARTIN, LOCKHEED_MARTIN)
        )
    )

    address = models.CharField(
        max_length=100,
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )


""" This class is used to create ONE to ONE key dependency"""


class User(models.Model):
    email = models.EmailField()
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True,
    )


""" This class is used to create MANY to MANY key dependency"""


class Project(models.Model):
    name = models.CharField(
        max_length=30,
    )

    deadline = models.DateField(
        null=True,
        blank=True,
    )

    employees = models.ManyToManyField(
        to=Employee
    )
