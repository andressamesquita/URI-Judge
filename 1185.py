def main():
	operacao = input()

	matriz = []
	for i in range(12):
		matriz.append([])
		for j in range(12):
			numero = float(input())
			matriz[i].append(numero)

	soma = 0
	qtd = 0
	for i in range(len(matriz)-1,-1,-1):
		for j in range(len(matriz[i])):
			if i+j < len(matriz)-1: #elementos acima da diagonal secundaria
				soma += matriz[i][j]
				qtd += 1

	if operacao == 'S':
		print('%.1f'%soma)
	else:
		media = soma/qtd
		print('%.1f'%media)



if __name__ == '__main__':
	main()