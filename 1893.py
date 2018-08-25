def main():

	entradas = input()
	m,n = [int(i) for i in entradas.split()]

	if n <= 2:
		print('nova')

	elif n <= 96:
		print('crescente')
	
	elif n <= 100:
		print('cheia')
	
	elif m >= 96 and n <= 3:
		print('minguante')

if __name__ == '__main__':
	main()