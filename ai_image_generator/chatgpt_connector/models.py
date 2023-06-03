from django.db import models

# Create your models here.
class Image(models.Model):
    prompt = models.CharField(max_length=200)
    size = models.CharField(max_length=10)