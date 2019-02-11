from django.db import models

# Create your models here.


class DogBreed(models.Model):
    name = models.CharField(max_length=200)
    activity = models.CharField(max_length=200)
    coat = models.CharField(max_length=200)
    drools = models.CharField(max_length=200)
    goodWC = models.CharField(max_length=200)
    grooming = models.CharField(max_length=200)
    intelligence = models.CharField(max_length=200)
    shedding = models.CharField(max_length=200)
    size = models.CharField(max_length=200)
    image = models.CharField(max_length=200)