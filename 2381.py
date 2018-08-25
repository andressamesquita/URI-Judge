def main():

	entradas = input()
	qtd,n = [int(i) for i in entradas.split()]

	chamada = []
	for i in range(qtd):
		nome = input()
		chamada.append(nome)
	
	
	ordem = chamada.sort(chamada[0][0])

	for nome in ordem:
		print (chamada[n])




if __name__ == '__main__':
	main()