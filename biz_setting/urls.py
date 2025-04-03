
from django.urls import path
from .views import SettingsAPIView

urlpatterns = [
    path('business_setting/', SettingsAPIView.as_view(), name='settings'),
]
