from django.db import models

# Create your models here.

class Product (models.Model):
    aff_url = models.CharField(max_length=300)
    title = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    oldprice = models.DecimalField(max_digits=10 , decimal_places=2)
    image = models.ImageField(upload_to="products_images")
   
    
    def __str__(self):
        return self.title

class Storbraf (models.Model):
    name = models.CharField(max_length=300)
    about_us = models.TextField(max_length=1000)
    privacy_policy = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name
    
class Contact (models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    subject = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.name