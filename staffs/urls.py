
from django.urls import path
from .views import StaffsAPIView

urlpatterns = [
    path('register_staff/', StaffsAPIView.as_view(), name='register_staff'),
]


