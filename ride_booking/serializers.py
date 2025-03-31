
from rest_framework import serializers
from .models import Order, Review, Expense



class OrderSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Order
        fields = [ 
            "from_location",
            "to_location",
            "order_type",
            "amount",
            "order_description",
            "customer_name",
            "phone_number",  
        ]
        
        
        

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
