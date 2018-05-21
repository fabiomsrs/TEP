from rest_framework import serializers
from .models import Game, GameCategory, Score, Player
from datetime import datetime
from django.utils import timezone

class GameSerializer(serializers.HyperlinkedModelSerializer):
	game_category =serializers.SlugRelatedField(queryset=GameCategory.objects.all(), slug_field='name')

	class Meta:
		model = Game
		fields = ('url','name', 'release_date', 'game_category')


class GameCategorySerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = GameCategory
		fields = ('url','pk', 'name', 'games')


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
	game =serializers.SlugRelatedField(queryset=Game.objects.all(),slug_field='name')
	player =serializers.SlugRelatedField(queryset=Player.objects.all(),slug_field='name')

	def validate(self, data):
		date_now = timezone.make_aware(datetime.now(), timezone.get_current_timezone())

		if data['score'] < 0:
			raise serializers.ValidationError('Score não pode ser negativo')
		if data['score_date'] > date_now:
			raise serializers.ValidationError('Data do score não pode estar no futuro!')

	class Meta:
		model = Score
		fields = (
		'url',
		'pk',
		'score',
		'score_date',
		'player',
		'game',
		)


class PlayerSerializer(serializers.HyperlinkedModelSerializer):
	scores = ScoreSerializer(many=True, read_only=True)
	class Meta:
		model = Player
		fields = (
		'url',
		'name',
		'gender',
		'scores',
		)
