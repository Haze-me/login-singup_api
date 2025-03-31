from django.contrib import admin
from .models import Review, Order, Expense

# Register your model
admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Expense)