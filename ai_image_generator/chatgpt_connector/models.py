from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Image(models.Model):
    prompt = models.TextField()
    size = models.CharField(max_length=10)
    url = models.CharField(max_length=200)