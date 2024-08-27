from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import get_user_model, authenticate
from .serializers import UserSerializer, UserCreateSerializer
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import get_object_or_404


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


# current logged-in user ki profile retrieve aur udate karta hai
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    """
    hum get_object method ko override karke ensure karte hain
    ki hamesha currently logged-in user ka object return ho.
    """
    def get_object(self):
        return self.request.user

# Ye view password reset request ko handle karta hai aur ek reset link generate karta hai.
class PasswordResetView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.filter(email=email).first()
        
        if user:
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = f"{request.scheme}://{request.get_host()}/api/users/reset-password/{uid}/{token}/"
            
            # Optional: Uncomment if you want to send the email
            # send_mail(
            #     'Password Reset Request',
            #     f'Click the link to reset your password: {reset_link}',
            #     settings.DEFAULT_FROM_EMAIL,
            #     [email]
            # )
            
            return Response({
                'message': 'Password reset request received',
                'reset_link': reset_link,
                'uid': uid,
                'token': token
            })
        
        return Response({'error': 'Email not found'}, status=400)
    

class PasswordResetConfirmView(APIView):
    def post(self, request, uidb64, token):
        try:
            # Decode UID and get user object
            uid = urlsafe_base64_decode(uidb64).decode()
            user = get_object_or_404(User, pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        
        # Check if the token is valid
        if user and default_token_generator.check_token(user, token):
            # Get the new password from request
            new_password = request.data.get('password')
            if new_password:
                user.set_password(new_password)
                user.save()
                return Response({'message': 'Password has been reset successfully'})
            return Response({'error': 'Password not provided'}, status=400)
        
        return Response({'error': 'Invalid or expired token'}, status=400)