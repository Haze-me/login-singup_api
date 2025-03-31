
import jwt
import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import RegisterSerializer, LoginSerializer, ChangePasswordSerializer
from rest_framework.generics import UpdateAPIView, CreateAPIView, GenericAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .serializers import ChangePasswordSerializer
from django_rest_passwordreset.views import ResetPasswordRequestToken, ResetPasswordConfirm



class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        
        # Generate JWT Token
        token = jwt.encode(
            {
                "user_id": user.id,
                "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24),
            },
            settings.SECRET_KEY,  # Use Django's SECRET_KEY
            algorithm="HS256"
        
        )
        
        # Generate verification link
        domain = self.request.get_host()
        verification_link = f"http://{domain}{reverse('verify-email')}?token={token}"

        # Send Email using Mailtrap SMTP
        send_mail(
    subject="Verify your Email",
    message=f"Click the link to verify your email: {verification_link}",  # Plain text version (fallback)
    from_email=settings.EMAIL_HOST_USER,  
    recipient_list=[user.email],
    fail_silently=False,
    html_message=f"""
        <p>Hello {user.first_name},</p>
        <p>Thank you for signing up! Please verify your email by clicking the link below:</p>
        <p><a href="{verification_link}" style="color: blue; font-weight: bold;">Verify Your Email</a></p>
        <p>If you did not sign up for this account, please ignore this email.</p>
        <br>
        <p>Best regards,<br>Haze</p>
    """,
)

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        email = request.data.get("email", "your email")  # Get the email from request data
        return Response(
             {"message": f"A verification email has been sent to {email}."},
            status=status.HTTP_201_CREATED
        )


class VerifyEmailView(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get("token")
        try:
            # Decode JWT token using Django's SECRET_KEY
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            
            # Fetch user
            user = CustomUser.objects.get(id=payload["user_id"])

            if user.is_active:
                return Response({"message": "Email is already verified."}, status=status.HTTP_200_OK)

            # Activate user
            user.is_active = True
            user.is_verified = True
            user.save()
            return Response({"message": "Email verified successfully!"}, status=status.HTTP_200_OK)
        
        except jwt.ExpiredSignatureError:
            return Response({"error": "Verification link has expired."}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.DecodeError:
            return Response({"error": "Invalid verification token."}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": f"Something went wrong: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]
        
        
        # Prevent login if email is not verified
        if not user.is_active:
            return Response(
                {"error": "Email not verified. Please check your email for verification link."},
                status=status.HTTP_403_FORBIDDEN
            )

        
        refresh = RefreshToken.for_user(user)
        
        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "message": "Login successful!"
            },
            status=status.HTTP_200_OK
        )




class CustomPasswordConfirmView(ResetPasswordConfirm, GenericAPIView):
    """
    Confirms the password reset using the token and sets a new password.
    """
    pass

class CustomPasswordResetView(ResetPasswordRequestToken, CreateAPIView):
    """
    Sends a password reset email with a token.
    """
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)  # Call parent method
        
        return Response({
            "message": "If the email exists, a password reset link has been sent."
        }, status=status.HTTP_200_OK)

User = get_user_model()

class ChangePasswordView(UpdateAPIView):

  #  API for changing user password. Requires authentication.
    permission_classes = [IsAuthenticated]
    serializer_class = ChangePasswordSerializer

    def get_object(self):
        return self.request.user  # Get the logged-in user

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            user.set_password(serializer.validated_data['new_password'])
            user.save()

            # Generate new JWT tokens (optional)
            refresh = RefreshToken.for_user(user)
            return Response({
                "message": "Password updated successfully!",
                "access": str(refresh.access_token),
                "refresh": str(refresh),
            }, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


