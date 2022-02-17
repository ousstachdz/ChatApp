from time import time
from django.contrib.auth.models import User

from rest_framework import serializers 

from .models import Message, Comment

class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta :
        model = User
        field = "__all__"

class MessageSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField(required=True, allow_blank=False, max_length=100)
    timestemp = serializers.ReadOnlyField()

    # class Meta :
    #     model = Message 
    #     field = '__all__'
        
class CommentSerializer (serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    content = serializers.CharField(required=True, allow_blank=False, max_length=100)
    timestemp = serializers.ReadOnlyField()
    class Meta :
        model = Comment 
        field = '__all__'