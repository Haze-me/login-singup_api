
from rest_framework import serializers
from .models import BusinessSetting, ContactSetting

class BusinessSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessSetting
        fields = '__all__'

class ContactSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactSetting
        fields = '__all__'

class SettingsSerializer(serializers.Serializer):
    business = BusinessSettingSerializer()
    contact = ContactSettingSerializer()

    def create(self, validated_data):
        business_data = validated_data.pop('business')
        contact_data = validated_data.pop('contact')
        
           # Ensure logo is optional
        business_logo = business_data.pop('logo', None)

        business = BusinessSetting.objects.create(**business_data)
        contact = ContactSetting.objects.create(**contact_data)

        return {"business": business, "contact": contact}

    def update(self, instance, validated_data):
        business_data = validated_data.get('business', {})
        contact_data = validated_data.get('contact', {})

        # Update BusinessSetting
        business = instance.get('business')
        if business:
            for attr, value in business_data.items():
                setattr(business, attr, value)
            business.save()

        # Update ContactSetting
        contact = instance.get('contact')
        if contact:
            for attr, value in contact_data.items():
                setattr(contact, attr, value)
            contact.save()

        return {"business": business, "contact": contact}
