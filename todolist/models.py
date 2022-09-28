from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user= models.ForeignKey(to=User, on_delete=models.CASCADE)
    date=models.DateField()
    title=models.CharField(max_length=200)
    description=models.TextField(null=True, max_length=200)
    is_finished=models.BooleanField(default=False)
