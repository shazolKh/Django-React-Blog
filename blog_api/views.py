from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import (
    SAFE_METHODS,
    DjangoModelPermissions,
    BasePermission,
    AllowAny,
    IsAuthenticated
)
from rest_framework import viewsets
from rest_framework.response import Response


# Create your views here.


class PostUserWritePermission(BasePermission):
    message = 'Only author can edit the post..'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.author == request.user


# Model ViewSet
class PostList(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    # queryset = Post.objects.filter(status='published').order_by('-published')

    # Custom queryset
    def get_queryset(self):
        return Post.objects.filter(status='published').order_by('-published')

    # get individual data
    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)


'''******************************************************************************'''
'''Normal Class Based Views'''
# class PostList(generics.ListCreateAPIView):
#     permission_classes = [DjangoModelPermissions]
#     permission_classes = [AllowAny]
#     queryset = Post.objects.filter(status='published').order_by('-published')
#     serializer_class = PostSerializer
#
#
# class PostDetails(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     permission_classes = [AllowAny]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


'''ViewSet'''
# class PostList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Post.objects.filter(status='published').order_by('-published')
#
#     def list(self, request):
#         serializer_class = PostSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)
#
#     def retrieve(self, request, pk=None):
#         post = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = PostSerializer(post)
#         return Response(serializer_class.data)

'''ViewSet Functions (Those will be under ViewSet classes)'''
# def list(self, request):
#     pass

# def create(self, request):
#     pass

# def retrieve(self, request, pk=None):
#     pass

# def update(self, request, pk=None):
#     pass

# def partial_update(self, request, pk=None):
#     pass

# def destroy(self, request, pk=None):
#     pass
