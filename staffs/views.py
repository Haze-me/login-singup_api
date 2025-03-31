
from rest_framework import generics
from .models import OrderInfo, EmploymentInfo, BasicInfo
from .serializers import OrderSerializer, BasicSerializer, EmploymentSerializer

class BasicCreateView(generics.CreateAPIView):
    queryset = BasicInfo.objects.all()
    serializer_class = BasicSerializer
    
    
class OrderCreateView(generics.CreateAPIView):
    queryset = OrderInfo.objects.all()
    serializer_class = OrderSerializer

class EmploymentCreateView(generics.CreateAPIView):
    queryset = EmploymentInfo.objects.all()
    serializer_class = EmploymentSerializer
