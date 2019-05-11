from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields =  ("name", "username", )# ('id', 'title', 'code', 'linenos', 'language', 'style')	
        fields = "__all__"