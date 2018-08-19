from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
	name = models.CharField(max_length=70)

	def save(self, *args, **kwargs):
		print("@@@@@@@@@",self.username)
		if not self.has_usable_password():
			self.set_password(self.password)			
		super(CustomUser, self).save(*args, **kwargs)


class Professor(CustomUser):
	degree = models.CharField(max_length = 30, null=True)

	class Meta:
		verbose_name = 'Professors'
		verbose_name_plural = 'Professors'

class Student(CustomUser):
	
	class Meta:
		verbose_name = 'Student'
		verbose_name_plural = 'Students'


class Discipline(models.Model):
	name = models.CharField(max_length=75)
	professor = models.ForeignKey('Professor', related_name='disciplines', on_delete=models.CASCADE)	


class Grade(models.Model):
	value = models.FloatField()
	year = models.IntegerField(null = True)
	semester = models.IntegerField(null = True)
	discipline = models.ForeignKey('Discipline', related_name='grades', on_delete=models.CASCADE)	
	student = models.ForeignKey('Student', related_name='grades', on_delete=models.CASCADE)

	# def save(self):
	# 	if self.discipline in [grade.discipline for grade in Grade.objects.filter(student=self.student)]:
	# 		pass
