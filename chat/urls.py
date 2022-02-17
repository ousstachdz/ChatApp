from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('users', views.UserList.as_view(),name="users"),
    path('messages', views.MessageList.as_view(),name="messages"),
    path('comments', views.CommentList.as_view(),name="comments"),
]
