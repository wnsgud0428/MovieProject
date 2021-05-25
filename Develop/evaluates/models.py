from django.db import models

# Create your models here.
class Evaluate(models.Model):
    user = models.CharField(max_length=10, default="youhoseong")
    keyword = models.CharField(max_length=100, default="")