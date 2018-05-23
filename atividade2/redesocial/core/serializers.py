from rest_framework import serializers
from .models import User, Post, Comment, Address


class CommentSerializer(serializers.HyperlinkedModelSerializer):
	post = serializers.SlugRelatedField(queryset=Post.objects.all(),slug_field='title')

	class Meta:
		model = Comment
		fields = ('pk','name','email','body','post',)


class PostListSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
	
	class Meta:
		model = Post
		fields = ('url','pk', 'title','body', 'user')
	

class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
	comments = CommentSerializer(many=True)	

	class Meta:
		model = Post
		fields = ('pk', 'title','body', 'user','comments')


class UserListSerializer(serializers.HyperlinkedModelSerializer):	
	
	class Meta:
		model = User
		fields = ('url','pk','name', 'username', 'email')


class UserDetailSerializer(serializers.HyperlinkedModelSerializer):	
	posts = PostListSerializer(many=True)
	class Meta:
		model = User
		fields = ('pk','name', 'username', 'email','posts')
