from django.db import models

from Taskify.utils import BaseContent
from Taskify_auth.models import User

# Create your models here.
STATUS_CHOICES = (
    ('no_progress', 'No Progress'),
    ('in_progress', 'In Progress'),
    ('completed', 'Completed')
)
PRIORITY_CHOICES = (
    ('', 'None'),
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High')
)


class SystemVariables(BaseContent):
    code = models.CharField(max_length=100, unique=True)
    title = models.CharField("Title", max_length=100)
    value = models.TextField("Value", max_length=1000)

    class Meta:
        unique_together = ["code", "title", "value"]

    def __str__(self):
        return f"{self.title}: {self.value}"


class Projects(BaseContent):
    name = models.CharField("Project Name", max_length=100)
    description = models.TextField("description", blank=True, null=True)
    secondary_avatar = models.FileField(upload_to="avatar", null=True)
    primary_avatar = models.FileField("Avatar", upload_to="avatar", blank=True, null=True,
        help_text="Recommended thumbnail size 800x400 (px)."
    )
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_avatar_url(self):
        if self.primary_avatar:
            return self.primary_avatar.url
        return self.secondary_avatar.url


class TasksLists(BaseContent):
    name = models.CharField("Title", max_length=255)
    description = models.TextField("Description", null=True, blank=True)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, null=True,related_name='task_list')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Task(BaseContent):
    task_list = models.ForeignKey(TasksLists, on_delete=models.CASCADE, null=True, related_name='tasks')
    name = models.CharField("Title", max_length=255)
    description = models.TextField("Description", null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='no_progress')
    priority = models.CharField(max_length=100, choices=PRIORITY_CHOICES, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks', null=True)


class TaskAttachments(BaseContent):
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    files = models.FileField(upload_to='tasks')