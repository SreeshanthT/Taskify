from django.urls import path,include

from rest_framework import routers
from rest_framework.authtoken import views

from Taskify_auth.views import (
    UserViewSet, CustomAuthToken, SignIn, GroupsViewSet, 
    SignUp,
)

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'group', GroupsViewSet)
urlpatterns =[
    path('',include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
    path('sign-in/', CustomAuthToken.as_view()),
    path('sign-up/', SignUp.as_view()),
    path('sign-in-session/', SignIn.as_view()),
    # path('roles/', GroupsView.as_view()),
]