def main():

	entradas = input()
	lista = [int(h) for h in entradas.split()]

	lista.sort()
	print (lista[1])


if __name__ == '__main__':
	main()