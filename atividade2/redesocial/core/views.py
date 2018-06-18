from django.shortcuts import get_object_or_404
from rest_framework import permissions, status, generics
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.throttling import ScopedRateThrottle
from .serializers import ProfileSerializer, ProfileDetailSerializer, ProfilePostsSerializer, PostSerializer, CommentSerializer
from .models import User, Post, Comment
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class Profiles(ViewSet):

	def list(self, request):        
		queryset = User.objects.all()
		serializer_class = ProfileSerializer(queryset, many=True,context={'request': request})		
		return Response(serializer_class.data)

	def retrieve(self, request, pk=None):
		queryset = User.objects.all()
		profile = get_object_or_404(queryset, pk=pk)
		serializer_class = ProfileSerializer(profile,context={'request': request})		
		return Response(serializer_class.data)	        

	def get_permissions(self):    
		if self.action == 'list' or self.action == 'retrieve':
			return [permissions.IsAuthenticated(),]
		else:
			return [permissions.IsAuthenticated(),]


class ProfileDetails(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = ProfileDetailSerializer


class ProfilePosts(ModelViewSet):
	queryset = User.objects.all()
	serializer_class = ProfilePostsSerializer


class Posts(ModelViewSet):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def get_permissions(self):
		return [permissions.IsAuthenticated(),IsOwnerOrReadOnly()]
        
	def get_queryset(self):
		try: 
			return Post.objects.filter(user=self.kwargs['profile_pk'])
		except KeyError:
			return Post.objects.all()


class Comments(ModelViewSet):
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer

	def get_permissions(self):
		return [permissions.IsAuthenticated(),IsOwnerOrReadOnly()]

	def get_queryset(self):
		try: 
			return Comment.objects.filter(post=self.kwargs['post_pk'])
		except KeyError:
			return Comment.objects.all()


class CustomAuthToken(ObtainAuthToken):
	throttle_scope = 'token'
	throttle_classes = (ScopedRateThrottle,)
	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data,context={'request': request})
		serializer.is_valid(raise_exception=True)
		user = serializer.validated_data['user']
		token, created = Token.objects.get_or_create(user=user)
	
		return Response({
			'token': token.key,
			'user_id': user.pk,
			'name': user.name
		})


class ApiRoot(generics.GenericAPIView):

    name = 'api-root'

    def get(self, request,*args, **kwargs):
        return Response({
            'profiles': reverse('profiles', request=request),
            'profile-posts': reverse('profile-posts', request=request),
            'profile-details': reverse('profile-details', request=request),
            'posts': reverse('posts', request=request),
            'comments': reverse('comments', request=request),
        })
