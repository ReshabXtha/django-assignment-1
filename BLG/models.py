from django.db import models
from datetime import datetime


# Create your models here.
class Author(models.Model):
    Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=30)
    Contact = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.Name)


class Blog(models.Model):
    Title = models.CharField(max_length=30)
    Created_at = models.DateTimeField(default=datetime.now())
    Updated_at = models.DateTimeField(default=None, blank=True)
    Author_name = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    Content = models.TextField()

    def __str__(self):
        return str(self.Title)
