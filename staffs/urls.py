
from django.urls import path
from .views import BasicCreateView, OrderCreateView, EmploymentCreateView

urlpatterns = [
    path('register_staff/', BasicCreateView.as_view(), name='register_staff'),
    path('order_info/', OrderCreateView.as_view(), name='order_info'),
    path('employ_info/', EmploymentCreateView.as_view(), name='employ_info')
]
