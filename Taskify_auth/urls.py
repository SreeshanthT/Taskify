from django.urls import path,include

from rest_framework import routers

from Taskify_auth.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
urlpatterns =[
    path('',include(router.urls)),
]