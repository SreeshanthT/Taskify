from rest_framework import serializers

from Taskify_main.models import Projects

class ProjectSerializers(serializers.ModelSerializer):

    class Meta:
        model = Projects
        fields = ['id','name','slug']