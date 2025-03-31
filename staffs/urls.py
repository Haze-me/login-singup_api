
from django.urls import path
from .views import StaffCreateView

urlpatterns = [
    path('register_staff/', StaffCreateView.as_view(), name='register_staff'),
]
