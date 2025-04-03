from django.contrib import admin
from .models import StaffInfo, EmploymentInfo, UploadDocument

# Register your model
admin.site.register(StaffInfo)
admin.site.register(EmploymentInfo)
admin.site.register(UploadDocument)
