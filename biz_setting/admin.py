from django.contrib import admin
from .models import BusinessSetting, ContactSetting

# Register your models here.

admin.site.register(BusinessSetting)
admin.site.register(ContactSetting)