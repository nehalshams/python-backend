from django.db import models

# Create your models here.

class Store(models.Model):
    bmp_id = models.CharField(max_length=100, unique=True)
    store_name = models.CharField(max_length=255)
