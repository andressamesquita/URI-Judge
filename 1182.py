def main():

	c = int(input())
	operacao = input()

	matriz = []
	for i in range(12):
		matriz.append([])
		for j in range(12):
			elemento = float(input())
			matriz[i].append(elemento)

	soma = 0
	for i in range(len(matriz)):
		soma += matriz[i][c]

	if operacao == 'S':
		print ('%.1f'%soma) 
	else:
		media = soma/12 
		print('%.1f'%media)

	
if __name__ == '__main__':
	main()