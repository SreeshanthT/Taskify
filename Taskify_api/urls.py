from django.urls import path,include

from rest_framework import routers

from Taskify_api.views import ProjectsView, TaskListView, TaskView

router = routers.DefaultRouter()
urlpatterns = [
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<str:project_slug>/',include([
        path('', ProjectsView.as_view(), name='project_with_instance'),
        path('task-list/',include([
            path('', TaskListView.as_view(), name='task_list'),
            path('<str:list_slug>/',include([
                path('',TaskListView.as_view(), name='task_list_with_instance'),
                path('task/',include([
                    path('',TaskView.as_view(),name='tasks'),
                    path('<str:task_slug>/',TaskView.as_view(),name='tasks_with_instance'),
                ])),
            ])),
        ])),
    ])),
]
