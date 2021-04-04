from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer


# Create your views here.


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.filter(status='published').order_by('-published')
    serializer_class = PostSerializer


class PostDetails(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
