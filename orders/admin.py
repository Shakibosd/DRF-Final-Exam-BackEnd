from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'flower', 'quantity', 'status', 'order_date', 'profit', 'revenue']

admin.site.register(Order, OrderAdmin)
    
    
    