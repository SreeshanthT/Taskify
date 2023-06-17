from django.urls import path, include
from Taskify_main.views.projects import ProjectListView, ProjectManageView

app_name = 'main'
urlpatterns_projects = [
    path("", ProjectListView.as_view(), name="project_list"),
    path("create/", ProjectManageView.as_view(method_name="manage"), name="project_add"),
    path("edit/<str:pk>/", ProjectManageView.as_view(method_name="manage"), name="project_edit")
]


urlpatterns = [
    path("projects/", include(urlpatterns_projects)),
]
