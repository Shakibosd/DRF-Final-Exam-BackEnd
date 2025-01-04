from rest_framework import serializers
from django.contrib.auth import password_validation

class ChangePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("New password and confirm password do not match.")
        password_validation.validate_password(data['new_password'], self.context['request'].user)
        return data
