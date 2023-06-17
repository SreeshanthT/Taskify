from django import forms
from django.core.files.storage import default_storage
from django.core.files import File
from io import BytesIO
from Taskify_main.models import Projects
from Taskify.utils import AvatarGenerator

import os
import requests


class ProjectManageForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ["name", "primary_avatar", "description"]

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(ProjectManageForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

    def save(self, commit=True, created_by=None):
        instance = super().save(commit=False)
        instance.created_by = self.request.user
        if commit:
            AVG = AvatarGenerator(title=instance.name)
            file = AVG.generate()
            absolute_url = default_storage.url(file)
            image_url = self.request.build_absolute_uri(absolute_url)

            resp = requests.get(image_url)
            fp = BytesIO()
            fp.write(resp.content)
            filename = os.path.basename(image_url)

            instance.secondary_avatar.save(filename, File(fp))
            instance.save()
            self.save_m2m()

        return instance
