from django.db import models

# Create your models here.
class MovieModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=40)
    director = models.CharField(max_length=10)
    keyword = ArrayField()