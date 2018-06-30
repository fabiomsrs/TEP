from rest_framework import serializers
from .models import Professor, Student, Discipline, Grade


class StudentSerializers(serializers.HyperlinkedModelSerializer):
	
	class Meta:
		model = Student
		fields = ('url','pk','name')


class ProfessorSerializers(serializers.HyperlinkedModelSerializer):
	# disciplines = DisciplineSerializers(many=True)

	class Meta:
		model = Professor
		fields = ('url','pk','name')


class DisciplineSerializers(serializers.HyperlinkedModelSerializer):
	professor = serializers.SlugRelatedField(queryset = Professor.objects.all(),slug_field='name')
	
	class Meta:
		model = Discipline
		fields = ('url','pk','name','professor')


class GradeSerializers(serializers.HyperlinkedModelSerializer):
	discipline = serializers.SlugRelatedField(queryset = Discipline.objects.all(),slug_field='name')
	student = serializers.SlugRelatedField(queryset = Student.objects.all(),slug_field='name')

	class Meta:
		model = Grade
		fields = ('url','pk','value','discipline','student')