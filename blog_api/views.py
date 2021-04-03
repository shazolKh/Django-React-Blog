from django.shortcuts import render
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializers


# Create your views here.


class PostList(generics.ListCreateAPIView):
    pass


class PostDetails(generics.RetrieveDestroyAPIView):
    pass

