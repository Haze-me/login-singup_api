from django.db import models
from django.core.validators import RegexValidator
# Create your models here.

currency_placement= [
        
        ('before', 'Before Amount'),
        ('after', 'After Amount'),
        
        ]


CURRENCY_CHOICES = [
    ("AFN", "Afghanistan - Afghan afghani (AFN)"),
    ("ALL", "Albania - Albanian lek (ALL)"),
    ("USD", "United States - US Dollar (USD)"),
    ("EUR", "Eurozone - Euro (EUR)"),
    ("INR", "India - Indian Rupee (INR)"),
    ("DZD", "Algeria - Algerian Dinar (DZD)"),
    ("AUD", "Australia - Australian Dollar (AUD)"),
    ("CAD", "Canada - Canadian Dollar (CAD)"),
    ("CNY", "China - Chinese Yuan (CNY)"),
    ("JPY", "Japan - Japanese Yen (JPY)"),
    ("NGN", "Nigeria - Nigerian Naira (NGN)"),
    ("ZAR", "South Africa - South African Rand (ZAR)"),
    ("KES", "Kenya - Kenyan Shilling (KES)"),
    ("GHS", "Ghana - Ghanaian Cedi (GHS)"),
    ("TND", "Tunisia - Tunisian Dinar (TND)"),
    ("MAD", "Morocco - Moroccan Dirham (MAD)"),
    ("ETB", "Ethiopia - Ethiopian Birr (ETB)"),
    ("XOF", "West African States - CFA Franc (XOF)"),
    ("UGX", "Uganda - Ugandan Shilling (UGX)"),
]


class BusinessSetting(models.Model):
    name = models.CharField(max_length=255)  # Business name
    start_date = models.DateField()
    select_currency = models.CharField(max_length=30, choices=CURRENCY_CHOICES, default="NGN")
    placement = models.CharField(max_length=20, choices=currency_placement, default='before')
    description = models.TextField()  # Business description
    logo = models.ImageField(upload_to='business_logos/', null=True, blank=True)  # Business logo

    
    def __str__(self):
        return self.name
    

class ContactSetting(models.Model):
    
    email = models.EmailField(max_length=255, unique=True, blank=False) 
    phone_number = models.CharField(
        max_length=15, 
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$')],  # Phone number validation using regex
        blank=False
    )
    country = models.CharField(max_length=100, blank=False)  
    state = models.CharField(max_length=100, blank=False)  
    address = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"{self.email} - {self.phone_number}"

