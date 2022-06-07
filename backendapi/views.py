from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import json
# model import
from rest_framework import status
from .models import plans, info,tickets,service,addon
# Serializer import
from .serializer import PlanSerializer, InfoSerializer,TicketsSerializer,ServiceSerializer,AddonSerializer
from rest_framework import serializers
# user authentication
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate


@api_view(['GET'])
def apioverview(request):
    api_urls = {
        'Plans': '/plan-api',
        'info': '/info-api',
        'Info-Post-Request': 'post-info',
        'plan-update':'plan-update/<str:pk>/',
        'Sumbit-info':'/sumbit-info',
        'new-plan':'new-plan',
        'user signup':'user-signup'
        
    }
    return Response(api_urls)
   
   
"""
Plan's API
"""

# Plan API below


@api_view(['GET'])
def fetchplan(request):
    result = plans.objects.all()
    serializer = PlanSerializer(result, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
def planUpdate(request, pk):
    task = plans.objects.get(id=pk)
    serializer = PlanSerializer(instance=task, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
    print(serializer.data)

    return Response(serializer.data)


@api_view(['POST'])
def new_plan(request):
    serializer = PlanSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"""
Info for main page
:news
:waiting time
:average reply
"""
# General Info api


@api_view(['GET'])
def Get_Info(request):
    res = info.objects.all()
    count = len(res)
    result = info.objects.filter(id=count)
    serializer = InfoSerializer(result, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def sumbit_info(request):
    serializer = InfoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


"""
Authentication function's
: Super Admin
: Normal's

"""


@api_view(['POST'])
def admin_auth_login(request):
    superusers = User.objects.filter(is_superuser=True)
    username = request.data['username']
    password = request.data['password']
    user = authenticate(username=username, password=password)
    if user.is_superuser:
        return Response({"authentication": "admin", "username": username})
    return Response({"authentication": "Fail"})

@api_view(['POST'])
def create_admin_user(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    user = User.objects.create(username= username,email= email,password=password, is_staff=True,is_superuser=True )
    user.set_password(password)
    user.save()
    return Response({ "Admin Created": username})


"""
Clients user API functions below
"""

@api_view(['POST'])
def user_signup(request):
    username = request.data['username']
    email = request.data['email']
    password = request.data['password']
    myuser = User.objects.create_user(username,email)
    myuser.set_password(password)
    myuser.save()
    return Response({ "User created": username})
   


"""
Tickets API

"""

@api_view(['POST'])
def sumbit_ticket(request):
    serializer = TicketsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def fetch_ticket(request,pk):
    result = tickets.objects.filter(user=pk)
    serializer = TicketsSerializer(result, many=True)
    return Response(serializer.data)

"""
Service API functions
"""
   
@api_view(['POST'])
def place_order(request):
    print(request.data)
    serializer = ServiceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
    return Response({ "User created"})
    
@api_view(['GET'])
def get_order(request,pk):
    result = service.objects.filter(user=pk)
    serializer = ServiceSerializer(result, many=True)
    return Response(serializer.data)