from django.db import models
from django.contrib.auth.models import User

class Flower(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    price = models.DecimalField(max_digits=11, decimal_places=2)
    image = models.CharField(default='', max_length=100)
    category = models.CharField(max_length=50)
    stock = models.PositiveIntegerField(default=1)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
