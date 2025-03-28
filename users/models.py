
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    username = None  # Remove username
    email = models.EmailField(unique=True)  # Ensure email is unique
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Remove username from required fields

    
    
    def __str__(self):
        return self.email
