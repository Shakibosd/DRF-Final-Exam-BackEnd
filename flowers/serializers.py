from rest_framework import serializers
from .models import Flower, Comment

class FlowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flower
        fields = ['id', 'title', 'description', 'price', 'image', 'category', 'stock']
        read_only_fields = ['id']

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class CommentSerializer(serializers.Serializer):
    flowerId = serializers.IntegerField()
    names = serializers.CharField(max_length=100)
    comment = serializers.CharField(max_length=1000)

    class Meta:
        model = Comment
        fields = ['flowerId', 'names', 'comment']

class CommentCheckOrderSerializer(serializers.Serializer):
    flowerId = serializers.IntegerField()

class ContactFormSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField()
    message = serializers.CharField(max_length=1000)

