from rest_framework import serializers

from Taskify_auth.models import User

class UserSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id','username', 'email', 'first_name','last_name']