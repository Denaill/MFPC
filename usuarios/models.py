from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    address = models.CharField(max_length=100, blank=True, null=True)
    number = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    cc = models.CharField(max_length=100, blank=True, null=True)
# Create your models here.
