from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import ProfileSerializer, ProfileDetailSerializer, ProfilePostsSerializer, PostSerializer, CommentSerializer
from .models import User, Post, Comment
# Create your views here.

class Profiles(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = ProfileSerializer


class ProfileDetails(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = ProfileDetailSerializer


class ProfilePosts(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = ProfilePostsSerializer

class Posts(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer	

	def get_queryset(self):
		try: 
			return Post.objects.filter(user=self.kwargs['profile_pk'])
		except KeyError:
			return Post.objects.all()


class Comments(ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def get_queryset(self):
		try: 
			return Comment.objects.filter(post=self.kwargs['post_pk'])
		except KeyError:
			return Comment.objects.all()