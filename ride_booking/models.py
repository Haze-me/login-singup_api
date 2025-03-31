
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
#import phonenumbers

class Order(models.Model):
    
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    order_type = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    order_description = models.TextField()
    customer_name = models.CharField(max_length=255)
    phone_number = PhoneNumberField(region='NG')


    def __str__(self):
        return f"Order by {self.customer_name}: From {self.from_location} to {self.to_location}"



class Review(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_review = models.TextField()

    def __str__(self):
        return f"Review by {self.customer_name}"
    
    
class Expense(models.Model):
    
     CATEGORY_CHOICES = [
         
        ('fuel', 'Fuel'),
        ('maintenace', 'Maintenace'),
        ('packaging', 'Packaging'),
        ('ticket', 'Ticket'),
        ('rider fee', 'Rider fee'),
        ('others', 'Others'),           
    ]
     
     
     expense_name = models.CharField(max_length=300)
     amount = models.DecimalField(max_digits=10, decimal_places=2)
     vendor = models.CharField(max_length=300)
     category = models.CharField(max_length=20, choices=CATEGORY_CHOICES) 
