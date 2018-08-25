def main():
	n = int(input())

	for i in range(1,n+1):
		entradas = input().split()
		nome = entradas[0]
		forca = int(entradas[1])

		if nome == 'Thor':
			print ('Y')
		else:
			print ('N')


if __name__ == '__main__':
	main()