from django.db import models

from movies import models as movie_model
# Create your models here.
class Recommend(models.Model):
    user = models.CharField(max_length=10, default="youhoseong")
    keyword = models.CharField(max_length=100, default="")
    movie = models.ManyToManyField(movie_model.MovieModel, related_name="recommend")

    