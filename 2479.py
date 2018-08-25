def main():

	n = int(input())
	nomes = []
	positivos = []
	negativos = []
	for a in range(n):
		entradas = input()
		sinal,nome = entradas.split()

		nomes.append(nome)	
		if sinal == '+':
			positivos.append(sinal)
		else:
			negativos.append(sinal)

	nomes.sort()
	for k in nomes:
		print(k)

	print('Se comportaram: %i | Nao se comportaram: %i' %(len(positivos),len(negativos)))


if __name__ == '__main__':
	main()