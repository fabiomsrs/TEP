import json
import os
import django

def main():
	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "redesocial.settings")
	django.setup()
	from core.models import User,Address,Comment,Post

	file = open('./db.json')
	data = json.load(file)	
	for user in data['users']:
		print()
		if not User.objects.filter(pk=user['id']).exists():
			User.objects.create(pk=user['id'],
				name=user['name'],
				email=user['email'],
				username=user['username'],
				address=Address.objects.create(street=user['address']['street'],suite=user['address']['suite'],city=user['address']['city'],zipcode=user['address']['zipcode']))

	print('Usuario criados\n')

	for post in data['posts']:
		if not Post.objects.filter(pk=post['id']).exists():
			Post.objects.create(pk=post['id'],
				title=post['title'],
				body=post['body'],
				user=User.objects.get(pk=post['userId']))

	print('Posts criados\n')	

	for comment in data['comments']:
		if not Comment.objects.filter(pk=comment['id']).exists():
			Comment.objects.create(pk=comment['id'],
				name=comment['name'],
				email=comment['email'],
				body=comment['body'],
				post=Post.objects.get(pk=comment['postId']))

	print('Comentarios criados\n')

if __name__ == '__main__':
	main()