from django.contrib.auth.models import User
from rest_framework import serializers 

from .models import Message, Comment

class UserSerializer (serializers.HyperlinkedModelSerializer):
    class Meta :
        model = User
        field = "__all__"

class MessageSerializer (serializers.Serializer):
    class Meta :
        model = Message 
        field = '__all__'
        
class CommentSerializer (serializers.Serializer):
    class Meta :
        model = Comment 
        field = '__all__'