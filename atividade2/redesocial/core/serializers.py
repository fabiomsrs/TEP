from rest_framework import serializers
from .models import User, Post, Comment, Address


class CommentSerializer(serializers.HyperlinkedModelSerializer):
	post = serializers.SlugRelatedField(queryset=Post.objects.all(),slug_field='title')

	class Meta:
		model = Comment
		fields = ('pk','name','email','body','post',)


class PostSerializer(serializers.HyperlinkedModelSerializer):
	user = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
	comments = serializers.SerializerMethodField(method_name='quantidade_comentarios')

	class Meta:
		model = Post
		fields = ('url','pk','title','body','user','comments')

	def quantidade_comentarios(self, obj):
		return obj.comments.all().count()
	

class ProfileSerializer(serializers.HyperlinkedModelSerializer):	
	
	class Meta:
		model = User
		fields = ('url','pk','name', 'username', 'email')


class ProfilePostsSerializer(serializers.HyperlinkedModelSerializer):	
	posts = PostSerializer(many=True)
	class Meta:
		model = User
		fields = ('pk','name', 'username', 'email','posts')


class ProfileDetailSerializer(serializers.HyperlinkedModelSerializer):	
	posts = serializers.SerializerMethodField('get_total_posts')
	comments = serializers.SerializerMethodField('get_total_comments')

	def get_total_posts(self, obj):
		return obj.posts.all().count()

	def get_total_comments(self, obj):
		count = 0
		for post in obj.posts.all():
			count += post.comments.all().count()
		return count

	class Meta:
		model = User
		fields = ('pk','name','posts','comments')
