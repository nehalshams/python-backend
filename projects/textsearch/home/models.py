from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    price = models.FloatField()
    brand = models.CharField(max_length=255, null=True, blank=True)
    sku = models.CharField(max_length=255)
    thumbnail = models.URLField(max_length=500)