"""
Book: Building RESTful Python Web Services
Chapter 2: Working with class based views and hyperlinked APIs in Django
Author: Gaston C. Hillar - Twitter.com/gastonhillar
Publisher: Packt Publishing Ltd. - http://www.packtpub.com
"""
from django.urls import path
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from games.models import Game, GameCategory, Score, Player
from games.serializers import GameSerializer, GameCategorySerializer, PlayerSerializer, ScoreSerializer

urlpatterns = [
    path('games/', ListCreateAPIView.as_view(queryset=Game.objects.all(), serializer_class=GameSerializer), name='game-list'),
    path('games/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view(queryset=Game.objects.all(), serializer_class=GameSerializer), name='game-detail'),
    path('game-categories/', ListCreateAPIView.as_view(queryset=GameCategory.objects.all(), serializer_class=GameCategorySerializer), name='gamecategory-list'),
    path('game-categories/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view(queryset=GameCategory.objects.all(), serializer_class=GameCategorySerializer), name='gamecategory-detail'),
    path('players/', ListCreateAPIView.as_view(queryset=Player.objects.all(), serializer_class=PlayerSerializer), name='player-list'),
	path('players/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view(queryset=Player.objects.all(), serializer_class=PlayerSerializer), name='player-detail'),
	path('scores/', ListCreateAPIView.as_view(queryset=Score.objects.all(), serializer_class=ScoreSerializer), name='score-list'),
	path('scores/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view(queryset=Score.objects.all(), serializer_class=ScoreSerializer), name='score-detail'),
	]
