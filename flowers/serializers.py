from rest_framework import serializers
from .models import Flower, Comment, PlantRevivalTip, CartItem
from django.contrib.auth.models import User

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['id', 'title', 'description', 'price', 'image', 'category', 'stock']
        read_only_fields = ['id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  
        fields = ['id', 'username']


class CommentsSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    flower = serializers.StringRelatedField()
    user = UserSerializer() 
    class Meta:
        model = Comment
        fields = '__all__'

        
class CommentSerializer(serializers.Serializer):
    flowerId = serializers.IntegerField()
    # names = serializers.CharField(max_length=100)
    comment = serializers.CharField(max_length=1000)
  
    class Meta:
        model = Comment
        fields = ['flowerId', 'user', 'comment']
        

class CommentEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body'] 


class CommentCheckOrderSerializer(serializers.Serializer):
    flowerId = serializers.IntegerField()


class ContactFormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=1000)


class FlowerCareTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantRevivalTip
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    flower_price = serializers.DecimalField(source="flower.price", read_only=True, max_digits=10, decimal_places=2)
    flower_image = serializers.CharField(source="flower.image", read_only=True)
    flower_description = serializers.CharField(source="flower.description", read_only=True)
    flower_stock = serializers.IntegerField(source="flower.stock", read_only=True)
    flower_category = serializers.CharField(source="flower.category", read_only=True)
    flower = serializers.StringRelatedField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'flower', 'flower_price', 'flower_image', 'flower_description', 'flower_stock', 'flower_category', 'added_at']