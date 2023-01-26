from django.urls import path,include

from rest_framework import routers

from Taskify_main.views import ProjectsView

router = routers.DefaultRouter()
urlpatterns = [
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<str:slug>/', ProjectsView.as_view(), name='project_with_instance'),
]