from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from Taskify_auth.models import User
from Taskify_auth.serializers import UserSerializers

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        print(request.user,"in")
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
        
class SignIn(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            logout(request)
            return Response({
                'first_name':request.user.first_name,
                'last_name':request.user.last_name,
            },status=200)
        else:
            return Response(status=400)
        
class GroupsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,*args,**kwargs):
        print(request.user)
        groups = Group.objects.all()
        return Response({})