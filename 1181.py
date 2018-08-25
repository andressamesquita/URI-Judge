def main():

	linha = int(input())
	operacao = input()

	coluna = [0] * 12
	matriz = [0] * 12

	
	for i in range(len(matriz)):
		matriz[i] = list(coluna)

	for i in range(len(matriz)):
		for j in range(len(matriz[i])):
			v = float(input())
			matriz[i][j] = v

	
	if operacao == 'S':
		soma = sum(matriz[linha])
		print (soma)
	else:
		media = sum(matriz[linha])/12
		print (media)
	

if __name__ == '__main__':
	main()