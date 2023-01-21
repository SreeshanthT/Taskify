from django.db import models
from django.contrib.auth.models import AbstractUser

from django_lifecycle import LifecycleModelMixin,hook,BEFORE_CREATE

from Taskify.utils import unique_slug_generator,BaseContent

# Create your models here.
class User(LifecycleModelMixin,AbstractUser):
    slug = models.SlugField(blank=True,max_length=255)
    
    class Meta:
        permissions = [
            ('change_password', 'Can change password'),
            ('set_permission', 'Can set permission'),
        ]

    def get_profile_pic(self):
        return(
            """
            https://ui-avatars.com/api/?background=0033C4&
            color=fff&size=256&name={}&rounded=true&bold=true
            """.format(self.username or self.email)
        )

    @hook(BEFORE_CREATE)
    def set_slug(self):
        self.slug = unique_slug_generator(self,self.username)