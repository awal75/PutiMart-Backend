from django.shortcuts import render
from django.contrib.auth import get_user_model,authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from .serializers import UserRegisterSerializer,UserLoginSerializer



# User=get_user_model()

# @api_view(['POST'])
# def user_register(request):

#     if request.method=='POST':
#         serializer=UserRegisterSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
    

# @api_view(['POST'])
# def login_view(request):

#     serializer=UserLoginSerializer(data=request.data)
    
#     serializer.is_valid(raise_exception=True)
    


#     return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
