from django.shortcuts import render, get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions

from Taskify.utils import get_object_or_none
from Taskify_main.models import Projects, TasksLists, Task
from Taskify_api.serializers import (
    ProjectSerializers, TasksListsSerializers, ProjectGlobalSerializers,
    TaskSerializers
)


# Create your views here.
class ProjectsView(APIView):
    queryset = Projects.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        project = get_object_or_none(Projects, slug=kwargs.get('project_slug'))
        if project:
            return Response(ProjectGlobalSerializers(project, many=False).data)
        project_serializer = ProjectGlobalSerializers(self.get_queryset(), many=True)
        return Response(project_serializer.data)

    def post(self, request, *args, **kwargs):
        project = get_object_or_none(Projects, slug=kwargs.get('project_slug'))
        serializer = ProjectSerializers(data=request.data, instance=project)
        if serializer.is_valid():
            PR = serializer.save()
            if not project:
                PR.created_by = self.request.user
                PR.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get_queryset(self):
        return Projects.objects.all()


class TaskListView(APIView):
    queryset = TasksLists.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        project = get_object_or_404(Projects, slug=kwargs.get('project_slug'))
        instance = get_object_or_none(project.task_list, slug=kwargs.get('list_slug'))

        if instance:
            return Response(TasksListsSerializers(instance, many=False).data)

        task_lists = TasksLists.objects.filter(project=project)
        return Response(TasksListsSerializers(task_lists, many=True).data)

    def post(self, request, *args, **kwargs):
        project = get_object_or_404(Projects, slug=kwargs.get('project_slug'))
        instance = get_object_or_none(TasksLists, project=project, slug=kwargs.get('list_slug'))
        serializer = TasksListsSerializers(data=request.data, instance=instance)

        if serializer.is_valid():
            TL = serializer.save()
            TL.project = project
            TL.created_by = self.request.user
            TL.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class TaskView(APIView):
    queryset = Task.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        task_list = get_object_or_404(TasksLists, slug=kwargs.get('list_slug'))
        instance = get_object_or_none(task_list.tasks, slug=kwargs.get('task_slug'))

        if instance:
            return Response(TaskSerializers(instance, many=False).data)

        task = Task.objects.filter(task_list=task_list)
        return Response(TaskSerializers(task, many=True).data)

    def post(self, request, *args, **kwargs):
        task_list = get_object_or_404(TasksLists, slug=kwargs.get('list_slug'))
        instance = get_object_or_none(task_list.tasks, slug=kwargs.get('task_slug'))
        serializer = TaskSerializers(data=request.data, instance=instance)

        if serializer.is_valid():
            TK = serializer.save()
            TK.task_list = task_list
            TK.created_by = self.request.user
            TK.save()
            return Response(serializer.data)
        return Response(serializer.errors)