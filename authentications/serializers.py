from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,login


User=get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','password','address']


class UserLoginSerializer(serializers.Serializer):
    email=serializers.EmailField()
    password=serializers.CharField(max_length=20)

    def create(self, validated_data):
        email=validated_data.get('email')
        password=validated_data.get('password')

        user=authenticate(email=email,password=password)

        if user:
            login(user)
            return user
        else:
            raise ValueError('unvalid creadintial')