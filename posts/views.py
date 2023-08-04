from django.shortcuts import render
from rest_framework import generics, permissions # new
from .models import Post
from .serializers import PostSerializer, UserSerializer # new
from .permissions import IsAuthorOrReadOnly # new
from django.contrib.auth import get_user_model # new
from rest_framework.permissions import IsAdminUser # new


class PostList(generics.ListCreateAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(generics.ListCreateAPIView): # new
     permission_classes = [IsAdminUser] # new
     queryset = get_user_model().objects.all()
     serializer_class = UserSerializer
class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    permission_classes = [IsAdminUser] # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    