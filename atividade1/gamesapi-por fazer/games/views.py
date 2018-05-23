from rest_framework.viewsets import ModelViewSet
from .models import Game, GameCategory, Score, Player
from .serializers import GameSerializer, GameCategorySerializer, PlayerSerializer, ScoreSerializer

class GameCategories(ModelViewSet):
	queryset = GameCategory.objects.all()
	serializer_class = GameCategorySerializer


class Games(ModelViewSet):
	queryset = Game.objects.all()
	serializer_class = GameSerializer


class Players(ModelViewSet):
	queryset = Player.objects.all()
	serializer_class = PlayerSerializer


class Scores(ModelViewSet):
	queryset = Score.objects.all()
	serializer_class = ScoreSerializer

