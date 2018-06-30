from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .models import Student, Professor, Discipline, Grade
from .serializers import StudentSerializers, ProfessorSerializers, DisciplineSerializers, GradeSerializers

# Create your views here.

class StudentView(ModelViewSet):
	queryset = Student.objects.all()
	serializer_class = StudentSerializers
	permission_classes = [permissions.IsAuthenticated(),]

	def get_permissions(self):    
		if self.action == 'list' or self.action == 'retrieve':
			return [permissions.IsAuthenticated(),]
		return [permissions.IsAdmin(),]


class ProfessorView(ModelViewSet):
	queryset = Professor.objects.all()
	serializer_class = ProfessorSerializers

	def get_permissions(self):    
		if self.action == 'list' or self.action == 'retrieve':
			return [permissions.IsAuthenticated(),]
		return [permissions.IsAdmin(),]


class DisciplineView(ModelViewSet):
	queryset = Discipline.objects.all()
	serializer_class = DisciplineSerializers

	def get_permissions(self):    
		if self.action == 'list' or self.action == 'retrieve':
			return [permissions.IsAuthenticated(),]
		return [permissions.IsAdmin(),]


class GradeView(ModelViewSet):
	queryset = Grade.objects.all()
	serializer_class = GradeSerializers

