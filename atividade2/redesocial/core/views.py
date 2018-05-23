from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import UserListSerializer, UserDetailSerializer, PostListSerializer, PostDetailSerializer, CommentSerializer
from .models import User, Post, Comment
# Create your views here.

class Users(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = UserListSerializer

	def get_serializer_class(self):			
		if self.action == 'retrieve':
			return UserDetailSerializer
		return UserListSerializer

class Posts(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostListSerializer

	def get_serializer_class(self):			
		if self.action == 'retrieve':
			return PostDetailSerializer
		return PostListSerializer


class Comments(ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer