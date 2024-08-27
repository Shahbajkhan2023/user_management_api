from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

"""
Yeh serializer user ki information ko read karne ke liye 
use hota hai. 
Yeh GET requests ke liye hai jo user ke details ko fetch 
karta hai.
"""
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name')

"""
Yeh serializer user creation ke liye use hota hai, 
jo POST requests ke liye hai aur new user ko create karta hai.
"""
class UserCreateSerializer(serializers.ModelSerializer):
    #  Iska matlab hai ki yeh field sirf data submit karte waqt use hoti hai aur output mein nahi dikhegi.
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', '')
        )
        return user
