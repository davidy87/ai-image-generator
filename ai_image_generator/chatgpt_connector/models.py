from django.db import models


# Create your models here.
class Image(models.Model):
    description = models.TextField()
    size = models.CharField(max_length=10)
    url = models.CharField(max_length=200)