from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


# Create your models here.

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    email_token = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=10, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    last_login_time = models.DateField(null=True, blank=True)
    last_logout_time = models.DateField(null=True, blank=True)
    is_subscriber = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

