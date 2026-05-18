from django.db import models

# Create your models here.

gender_choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
]


class College(models.Model):
    college_name = models.CharField(max_length=100)
    college_address = models.CharField(max_length=200)
class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=10, choices=gender_choices, default='Male')
    age = models.PositiveIntegerField(null=True, blank=True)
    # date_of_birth = models.DateField(null=True)
    profile_image = models.ImageField(null=True, blank=True, upload_to='students/')
    file = models.FileField(upload_to='files/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name='students', null=True, blank=True)


class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    published_date = models.DateField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)

class Brand(models.Model):
    brand_name = models.CharField(max_length=50)

class Product(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)