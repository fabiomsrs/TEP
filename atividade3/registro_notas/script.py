import json
import os
import django

def main():
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "registro_notas.settings")
	django.setup()
	from core.models import Professor,Student,Discipline,Grade

	file = open('./bd.json')
	data = json.load(file)	
	print('carregou file')
	for user in data['professors']:
		print()		
		p = Professor.objects.create(name=user['name'],
			email=user['email'],
			username=user['username'])
		p.set_password('123456')
		p.save()
	for user in data['students']:
		print()		
		s = Student.objects.create(name=user['name'],
			email=user['email'],
			username=user['username'])
		s.set_password('123456')
		s.save()

	print('Professores e alunos criados\n')

	for discipline in data['disciplines']:		
		Discipline.objects.create(name=discipline['name'],			
			professor=Professor.objects.get(username=discipline['professor']))

	print('disciplinas criadas\n')	

	for grade in data['grades']:		
		Grade.objects.create(
			value=grade['value'],
			year=grade['year'],
			semester=grade['semester'],
			discipline=Discipline.objects.get(pk=grade['discipline']),
			student=Student.objects.get(username=grade['student']))

	print('Notas criadas\n')

if __name__ == '__main__':
	main()