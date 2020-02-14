from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(default="", max_length=512)


class Student(models.Model):
    course = models.CharField(default="", max_length=512)


class Admin(models.Model):
    access_level = models.IntegerField()


class Resident(models.Model):
    occupation = models.CharField(default="", max_length=512)
