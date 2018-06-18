import requests

def main():
	quantidade = int(input('Quantidade: '))
	for i in range(quantidade):
		r = requests.get('http://localhost:8000/')
		print(r.status_code)


if __name__ == '__main__':
	main()