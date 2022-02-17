from django.contrib import admin

from .models import Message, Comment, Post

admin.site.register(Message)
admin.site.register(Comment)
admin.site.register(Post)

# Register your models here.
