
from rest_framework import serializers
from .models import StaffInfo, UploadDocument, EmploymentInfo

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffInfo
        fields = '__all__'
        
class EmploymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentInfo
        fields = '__all__'
                
class UploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadDocument
        fields = '__all__'

class StaffsSerializer(serializers.Serializer):
    staff = StaffSerializer()
    employment = EmploymentSerializer()
    upload = UploadSerializer()

    def create(self, validated_data):
        staff_data = validated_data.get('staff', {})
        employment_data = validated_data.get('employment', {})
        upload_data = validated_data.get('upload', {})

        staff = StaffInfo.objects.create(**staff_data)
        employment = EmploymentInfo.objects.create(**employment_data)
        upload = UploadDocument.objects.create(**upload_data)

        return {"staff": staff, "employment": employment, "upload": upload}

    def update(self, instance, validated_data):
        staff_data = validated_data.get('staff', {})
        employment_data = validated_data.get('employment', {})
        upload_data = validated_data.get('upload', {})

        # Update StaffInfo
        staff = instance.staff
        for attr, value in staff_data.items():
            setattr(staff, attr, value)
        staff.save()

        # Update EmploymentInfo
        employment = instance.employment
        for attr, value in employment_data.items():
            setattr(employment, attr, value)
        employment.save()

        # Update UploadDocument
        upload = instance.upload
        for attr, value in upload_data.items():
            setattr(upload, attr, value)
        upload.save()

        return {"staff": staff, "employment": employment, "upload": upload}
