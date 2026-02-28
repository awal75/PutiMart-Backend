from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer,UserSerializer as BaseUserSerializer


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields=('id','first_name','last_name','email','password','address','phone_number')



class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        ref_name='customusercreateserializer'
        fields=('id','email','first_name','last_name','phone_number','address')
