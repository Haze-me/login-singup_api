
from rest_framework import generics
from .models import Order, Review, Expense
from .serializers import OrderSerializer, ReviewSerializer, ExpenseSerializer

class ExpenseCreateView(generics.ListCreateAPIView): # ListCreateAPIView Supports both GET and POST
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    
    
class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class ReviewCreateView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
