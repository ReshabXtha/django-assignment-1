from django.db import models
from datetime import datetime
from user.models import Profile


# Create your models here.


class Blog(models.Model):
    Title = models.CharField(max_length=30)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)
    Author_name = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    Content = models.TextField()

    def __str__(self):
        return '{}    {}    {}'.format(self.Title,self.Created_at,self.Updated_at)
