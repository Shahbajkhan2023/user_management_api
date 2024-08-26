from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate
from django.core.mail import send_mail
from django.conf import settings
from .serializers import UserSerializer, UserCreateSerializer

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=400)


class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            # Implement password reset logic here (e.g., send email with reset link)
            send_mail(
                'Password Reset Request',
                'Click the link to reset your password: <link>',
                settings.DEFAULT_FROM_EMAIL,
                [email]
            )
            return Response({'message': 'Password reset email sent'})
        return Response({'error': 'Email not found'}, status=400)
