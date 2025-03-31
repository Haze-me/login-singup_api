from django.contrib import admin
from .models import BasicInfo, EmploymentInfo, OrderInfo

# Register your model
admin.site.register(BasicInfo)
admin.site.register(EmploymentInfo)
admin.site.register(OrderInfo)