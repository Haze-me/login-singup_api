from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BusinessSetting, ContactSetting
from .serializers import SettingsSerializer, BusinessSettingSerializer, ContactSettingSerializer

# Create your views here.

class SettingsAPIView(APIView):
    def get(self, request):
        business = BusinessSetting.objects.first()
        contact = ContactSetting.objects.first()
        data = {
            "business": BusinessSettingSerializer(business).data if business else None,
            "contact": ContactSettingSerializer(contact).data if contact else None
        }
        return Response(data)

    def post(self, request):
        serializer = SettingsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Settings saved successfully", "data": serializer.data}, status=201)
        return Response(serializer.errors, status=400)
