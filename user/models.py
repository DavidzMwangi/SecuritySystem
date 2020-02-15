from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from residence.models import Residence


class User(AbstractUser):
    pass
    phone_no = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    user_type = models.IntegerField(default=0)


class Student(models.Model):
    course = models.CharField(max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reg_no = models.CharField(max_length=250)
    year_of_study = models.CharField(max_length=250)
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)


class Admin(models.Model):
    access_level = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Resident(models.Model):
    occupation = models.CharField(default="", max_length=512)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    residence = models.ForeignKey(Residence, on_delete=models.CASCADE)
