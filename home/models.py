from django.db import models
from django.urls import reverse

# Create your models here.
STATUS = (('active','Active'),('inactive','Inactive'))
LABEL = (('new','new'),('hot','hot'),('','default'))
class Category(models.Model):
    name = models.CharField(max_length = 200)
    logo = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 300)
    status = models.CharField(choices = STATUS,max_length = 200)
    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS, max_length=200)
    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    rank = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=200)
    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    status = models.CharField(choices=STATUS, max_length=200)
    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=400)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    image = models.ImageField(upload_to='media')
    status = models.CharField(choices=STATUS, max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    label = models.CharField(max_length=200,choices=LABEL,blank=True)
    description = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    slug = models.CharField(max_length=300)
    def __str__(self):
        return self.name

    def add_to_cart(self):
        return reverse('cart:add-to-cart',kwargs = {'slug':self.slug})
