from django.db import models
from django.contrib.auth.models import User
from flowers.models import Flower
from .constants import ORDER_STATUS
from decimal import Decimal

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flower = models.ForeignKey(Flower, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(choices=ORDER_STATUS, max_length=50, default='Pending')
    order_date = models.DateTimeField(auto_now_add=True)
    revenue = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    profit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    def __str__(self):
        return f'{self.id} {self.user.username}'
    
    def save(self, *args, **kwargs): 
        self.revenue = self.flower.price * self.quantity
        self.profit = self.revenue * Decimal('0.20') 
        super().save(*args, **kwargs)
