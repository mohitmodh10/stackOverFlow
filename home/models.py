from django.db import models
from django.db.models.deletion import CASCADE
from datetime import datetime
from django.contrib.auth.models import AbstractUser

from stackOverFlow.manager import UserManager


class UserModel(AbstractUser):
    first_name = models.CharField(max_length=64,null= False)
    last_name = models.CharField(max_length=64, null= False)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128,null=False)
    username = None

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email 

