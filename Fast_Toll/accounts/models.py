from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    car_number = models.CharField(max_length=200, blank=True)
