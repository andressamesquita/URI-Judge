def main():

	n = int(input())

	for i in range(n):
		qtd = int(input())

		for j in range(qtd):
			feed = int(input())

			if feed == 1:
				print('Rolien')
			elif feed == 2:
				print('Naej')
			elif feed == 3:
				print('Elehcim')
			elif feed == 4:
				print('Odranoel')

if __name__ == '__main__':
	main()