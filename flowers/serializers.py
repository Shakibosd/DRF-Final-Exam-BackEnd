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
    comment = serializers.CharField(max_length=1000)
  
    class Meta:
        model = Comment
        fields = ['flowerId', 'user', 'comment']
        

class CommentEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'body'] 


class CommentCheckOrderSerializer(serializers.Serializer):
    flowerId = serializers.IntegerField(required=True)
    

class ContactFormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=1000)


class FlowerCareTipSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlantRevivalTip
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    flower = FlowerSerializer()
    flower = serializers.StringRelatedField()
    
    class Meta:
        model = CartItem
        fields = ['id', 'flower', 'quantity', 'added_at']