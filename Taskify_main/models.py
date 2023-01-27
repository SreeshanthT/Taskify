from django.db import models

from Taskify.utils import BaseContent
from Taskify_auth.models import User

# Create your models here.
class Projects(BaseContent):
    name = models.CharField("Project Name",max_length=100)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)