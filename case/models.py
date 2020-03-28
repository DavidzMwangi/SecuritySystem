from django.db import models

# Create your models here.
from user.models import User


class Category(models.Model):
    name = models.CharField(max_length=250)
    level = models.IntegerField()
    description = models.CharField(max_length=512)

    def __str__(self):
        return self.name


class Case(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.IntegerField()
    description = models.CharField(max_length=512)
    location = models.CharField(max_length=250)
    time = models.DateTimeField()
    picture = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
