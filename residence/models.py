from django.db import models


# Create your models here.
class Residence(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    care_taker_text = models.CharField(max_length=250)
