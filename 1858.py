def main():
	n = int(input())
	entradas = input()

	lista = [int(i) for i in entradas.split()]

	menor = min(lista)
	indice = lista.index(menor)

	print(indice+1)



if __name__ == '__main__':
	main()