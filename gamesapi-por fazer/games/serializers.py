from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Game

class GameSerializer(serializers.ModelSerializer):
	name = serializers.CharField(max_length=200, validators=[UniqueValidator(queryset=Game.objects.all())])
	game_category = serializers.CharField(max_length=200, allow_blank=False)
	class Meta:
		model = Game
		fields = ('id','name', 'release_date', 'game_category')		