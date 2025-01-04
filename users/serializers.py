from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    profile_img = serializers.CharField(source='profile.profile_img', read_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'profile_img']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)   
        return user

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    profile_img = serializers.URLField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'profile_img']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        profile_img = validated_data.pop('profile_img', None)
        user = User.objects.create_user(**validated_data)

        user.is_active = False 
        user.save()

        Profile.objects.create(
            user=user,
            profile_img=profile_img,
        )
        
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

