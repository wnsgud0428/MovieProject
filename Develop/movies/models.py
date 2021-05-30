from django.db import models

# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=20, blank=False)
    weight = models.CharField(max_length=10, blank=False)

class Director(models.Model):
    name = models.CharField(max_length=20, blank=False)
    weight = models.CharField(max_length=10, blank=False)

class Genre(models.Model):
    name = models.CharField(max_length=20, blank=False)
    weight = models.CharField(max_length=10, blank=False)


