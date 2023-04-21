from rest_framework import serializers

from Taskify_main.models import Projects, TasksLists, Task
from Taskify_auth.models import User


class UsersListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['slug', 'full_name']


class ProjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ['id','name','slug']


class TasksListsSerializers(serializers.ModelSerializer):
    
    project = ProjectSerializers(read_only = True, many=False)
    created_by = UsersListSerializer(read_only = True, many=False)
    
    class Meta:
        model = TasksLists
        fields = ['project','name','description','created_by','slug']


class TaskSerializers(serializers.ModelSerializer):
    
    created_by = UsersListSerializer(read_only = True, many=False)
    assigned_to = UsersListSerializer(read_only = True, many=False)
    task_list = TasksListsSerializers(read_only = True, many=False)
    
    class Meta:
        model = Task
        fields = ['name','description','due_date','status','priority','slug', 'assigned_to', 'created_by','task_list']


class TaskGlobalSerializers(serializers.ModelSerializer):
    
    created_by = UsersListSerializer(read_only = True, many=False)
    assigned_to = UsersListSerializer(read_only = True, many=False)
    
    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'status', 'priority', 'slug',
            'assigned_to', 'created_by']
        

class TasksListsGlobalSerializers(serializers.ModelSerializer):
    
    created_by = UsersListSerializer(read_only = True, many=False)
    tasks = TaskGlobalSerializers(read_only = True, many=True)
    
    class Meta:
        model = TasksLists
        fields = ['name','description','slug','created_by','tasks']
        
class ProjectGlobalSerializers(serializers.ModelSerializer):

    task_list = TasksListsGlobalSerializers(many = True, read_only = True)
    created_by = UsersListSerializer(read_only = True, many=False)
    
    class Meta:
        model = Projects
        fields = ['name','slug','created_by','task_list']
        