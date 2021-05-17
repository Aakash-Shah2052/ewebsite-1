from django.db import models
from home.models import Item

class Cart(models.Model):
    username = models.CharField(max_length = 400)
    items = models.ForeignKey(Item,on_delete=models.CASCADE)
    slug = models.CharField(max_length = 400)
    quantity = models.IntegerField(default = 1)
    total = models.IntegerField()
    checkout = models.BooleanField(default = False)

    def __str__(self):
        return self.username
