from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    location = models.CharField(
        verbose_name="location",
        max_length=100,
        blank=True,
        null=True
    )
    number = models.CharField(
        verbose_name="Phone Number",
        max_length=20,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.username
