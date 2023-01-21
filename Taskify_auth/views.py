from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.views import APIView

from Taskify_auth.models import User
from Taskify_auth.serializers import UserSerializers

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
