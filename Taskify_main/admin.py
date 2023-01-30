from django.contrib import admin

from .models import Projects, Task, TasksLists

# Register your models here.

admin.site.register(Projects)
admin.site.register(Task)
admin.site.register(TasksLists)