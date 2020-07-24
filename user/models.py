from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Profile(AbstractUser):
    profile_pic = models.ImageField(blank=True)
    groups = None
    user_permissions = None

    def __str__(self):
        return str(self.username)

