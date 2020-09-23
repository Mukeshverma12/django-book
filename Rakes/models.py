from django.db import models
from django.urls import reverse


# Create your models here.

class Post(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.CharField(max_length=30)
    order=models.TextField()
    area=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('createview')


class Product(models.Model):
    nameofProduct=models.CharField(max_length=50)
    price = models.CharField(max_length=100)
    images=models.ImageField(upload_to='photo/')
    discription=models.CharField(max_length=200)

    def __str__(self):
        return self.nameofProduct



