
from rest_framework import serializers
from .models import StaffInfo

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffInfo
        fields = '__all__'


