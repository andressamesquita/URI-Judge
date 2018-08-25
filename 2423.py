def main():

	entradas = input()
	lista = [int(i) for i in entradas.split()]

	trigo,ovos,leite = lista[0]//2,lista[1]//3,lista[2]//5
	qtd = [trigo,ovos,leite]

	menor = min(qtd)
	print(menor)


if __name__ == '__main__':
	main()