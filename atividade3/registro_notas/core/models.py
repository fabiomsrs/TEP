from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
	name = models.CharField(max_length=70)	


class Professor(CustomUser):
	pass


class Student(CustomUser):
	pass


class Discipline(models.Model):
	name = models.CharField(max_length=75)
	professor = models.ForeignKey('Professor', related_name='disciplines', on_delete=models.CASCADE)	


class Grade(models.Model):
	value = models.FloatField()
	discipline = models.ForeignKey('Discipline', related_name='grades', on_delete=models.CASCADE)	
	student = models.ForeignKey('Student', related_name='grades', on_delete=models.CASCADE)
