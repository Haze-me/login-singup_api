
from rest_framework import generics
from .models import StaffInfo
from .serializers import StaffSerializer

class StaffCreateView(generics.CreateAPIView):
    queryset = StaffInfo.objects.all()
    serializer_class = StaffSerializer
    
