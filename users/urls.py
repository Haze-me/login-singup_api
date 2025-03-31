

from django.urls import path
from .views import (RegisterView, VerifyEmailView, LoginView,
CustomPasswordConfirmView, CustomPasswordResetView, ChangePasswordView)

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('verify-email/', VerifyEmailView.as_view(), name='verify-email'),
    path('login/', LoginView.as_view(), name='login'),
    # password reset    
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password-reset'),
    path('password-reset-confirm/', CustomPasswordConfirmView.as_view(), name='password-reset-confirm'),
]

  