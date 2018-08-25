def main():

	operacao = input()

	matriz = []
	for i in range(12):
		matriz.append([])
		for j in range(12):
			elemento = float(input())
			matriz[i].append(elemento)

	soma = 0
	qtd = 0
	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			if i < j:
				soma += matriz[i][j]
				qtd += 1

	if operacao == 'S':
		print('%.1f'%soma)
	else:
		media = soma/qtd
		print ('%.1f'%media)


if __name__ == '__main__':
	main()