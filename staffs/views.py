
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import StaffInfo, EmploymentInfo, UploadDocument
from .serializers import StaffSerializer, EmploymentSerializer, UploadSerializer, StaffsSerializer

# Create your views here.

class StaffsAPIView(APIView):
    def get(self, request):
        staff = StaffInfo.objects.first()
        employment = EmploymentInfo.objects.first()
        upload = UploadDocument.objects.first()
        data = {
            "staff": StaffSerializer(staff).data if staff else None,
            "employment": EmploymentSerializer(employment).data if employment else None,
            "upload": UploadSerializer(upload).data if upload else None
        }
        return Response(data)

    def post(self, request):
        serializer = StaffsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Settings saved successfully", "data": serializer.data}, status=201)
        return Response(serializer.errors, status=400)
