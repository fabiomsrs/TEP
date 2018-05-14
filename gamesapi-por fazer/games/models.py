from django.db import models
from datetime import datetime
from django.utils import timezone
from rest_framework.exceptions import MethodNotAllowed

# Create your models here.
class Game(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200, blank=True, default='')
	release_date = models.DateTimeField()
	game_category = models.CharField(max_length=200, blank=True, default='')
	played = models.BooleanField(default=False)

	class Meta:
		ordering = ('name',)

	def delete(self):    
		time = timezone.make_aware(datetime.now(),timezone.get_current_timezone())

		if self.release_date < time:
			raise MethodNotAllowed('DELETE', detail='Não é possivel excluir jogos que já foram lançados', code='405')

		super(Game, self).delete()
