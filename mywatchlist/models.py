# Create your models here.
from django.db import models

class ListFilm(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=200)
    rating = models.FloatField()
    release_date = models.DateField()
    review= models.TextField()
