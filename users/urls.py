

from django.urls import path
from .views import RegisterView, VerifyEmailView, LoginView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('login/', LoginView.as_view(), name='login'),
]
