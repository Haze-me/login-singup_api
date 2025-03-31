

from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = self.context['request'].user
        if not check_password(data['old_password'], user.password):
            raise serializers.ValidationError({"old_password": "Incorrect old password."})
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "Passwords do not match."})
        return data



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')  # Remove confirm_password
        user = CustomUser.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            is_active=False, # Require email verification before login
            is_verified=False,
        )
        user.set_password(validated_data['password'])  # Hash password
        user.save()
        return user
    
    



class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")
        
        # First, check if the user exists
        user = CustomUser.objects.filter(email=email).first()

        if user and not user.is_verified:  # Prioritize checking if email is verified
            raise serializers.ValidationError({"error": "Email not verified. Please check your inbox."})

        # Authenticate user
        user = authenticate(username=email, password=password)
        
        if user is None:
            raise serializers.ValidationError("Invalid email or password.")
  
        return {"user": user}  # Return a dictionary with the user
    
    
