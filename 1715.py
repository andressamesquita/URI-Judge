def main():

	entradas = input()
	m,n = [int(i) for i in entradas.split()]
	matriz = []

	for i in range(m):
		entrad = input()
		vetores = [int(k) for k in entrad.split()]
		matriz.append(vetores)

	jogadores = 0	
	for i in range(len(matriz)):
		vezes = matriz[i].count(0)
		if vezes == 0:
			jogadores += 1
		
	print(jogadores)


if __name__ == '__main__':
	main()