from rest_framework import serializers
from .models import Order

class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['flower', 'quantity']

class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    flower = serializers.StringRelatedField()
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'flower', 'quantity', 'status', 'order_date']

class OrderSerializerForCreate(serializers.Serializer):
    user_id = serializers.IntegerField()
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()