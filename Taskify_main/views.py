from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from Taskify.utils import get_object_or_none
from Taskify_main.models import Projects
from Taskify_main.serializers import ProjectSerializers

# Create your views here.
class ProjectsView(APIView):
    queryset = Projects.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request,*args,**kwargs):
        project = get_object_or_none(Projects,slug = kwargs.get('slug'))
        if project:
            return Response(ProjectSerializers(project, many = False).data)
        project_serializer = ProjectSerializers(self.get_queryset(), many = True)
        return Response(project_serializer.data)

    def post(self,request,*args,**kwargs):
        project = get_object_or_none(Projects,slug = kwargs.get('slug'))
        serializer = ProjectSerializers(data = request.data, instance=project)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get_queryset(self):
        return Projects.objects.all()

    