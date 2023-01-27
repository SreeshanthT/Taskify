from django.db import models

from Taskify.utils import BaseContent
from Taskify_auth.models import User

# Create your models here.
STATUS_CHOICES = (
    ('no_progress','No Progress'),
    ('in_progress','In Progress'),
    ('completed','Completed')
)
PRIORITY_CHOICES = (
    ('','None'),
    ('low','Low'),
    ('medium','Medium'),
    ('high','High')
)

class Projects(BaseContent):
    name = models.CharField("Project Name",max_length=100)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
class TasksLists(BaseContent):
    name = models.CharField("Title",max_length=255)
    description = models.TextField("Description",null=True,blank=True)
    project = models.ForeignKey(Projects,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    
class Task(BaseContent):
    task_list = models.ForeignKey(TasksLists,on_delete=models.CASCADE)
    name = models.CharField("Title",max_length=255)
    description = models.TextField("Description",null=True,blank=True)
    assinged_to = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    due_date = models.DateField(null=True,blank=True)
    status = models.CharField(max_length=100,choices=STATUS_CHOICES,default='no_progress')
    priority = models.CharField(max_length=100,choices=PRIORITY_CHOICES,null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_tasks')

class TaskAttachments(BaseContent):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    files = models.FileField(upload_to='tasks')