from rest_framework import generics
from .models import Game, GameCategory, Score, Player
from .serializers import GameSerializer, GameCategorySerializer, PlayerSerializer, ScoreSerializer

class GameCategoryList(generics.ListCreateAPIView):
	queryset = GameCategory.objects.all()
	serializer_class = GameCategorySerializer
	name = 'gamecategory-list'


class GameCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = GameCategory.objects.all()
	serializer_class = GameCategorySerializer
	name = 'gamecategory-detail'


class GameList(generics.ListCreateAPIView):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	name = 'game-list'


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Game.objects.all()
	serializer_class = GameSerializer
	name = 'game-detail' 


class PlayerList(generics.ListCreateAPIView):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
	name = 'player-list'


class PlayerDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer
	name = 'player-detail'


class ScoreList(generics.ListCreateAPIView):
	queryset = Score.objects.all()
	serializer_class = ScoreSerializer
	name = 'score-list'


class ScoreDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Score.objects.all()
	serializer_class = ScoreSerializer
	name = 'score-detail'

