from django.urls import path, include

from rest_framework import routers
from rest_framework.authtoken import views

from Taskify_auth.views.api import (
    UserViewSet, CustomAuthToken, SignIn, GroupsViewSet, 
    SignUp,
)
from Taskify_auth.views.web import login_view, logout_view, dashboard

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'group', GroupsViewSet)

urlpatterns_api = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('sign-in/', CustomAuthToken.as_view()),
    path('sign-up/', SignUp.as_view()),
    path('sign-in-session/', SignIn.as_view()),
    # path('roles/', GroupsView.as_view()),
]

urlpatterns_app = [
    path('login', login_view, name='login-page'),
    path('logout', logout_view, name='logout-page'),
    path('', dashboard, name='dashboard')
]

urlpatterns =[
    path("api/", include(urlpatterns_api)),
    path("", include(urlpatterns_app)),
]
