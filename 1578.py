def main():
	n = int(input())
	teste = 4
	for i in range(n):
		m = int(input())
	
		
		matriz = []
		for j in range(m):
			entradas = input()
			coluna = [int(i) for i in entradas.split()]
			matriz.append(coluna)

				
		print('Quadrado da matriz #%i:'%teste)
		for i in range(len(matriz)):
			for j in range(len(matriz[i])):
				matriz[i][j] = matriz[i][j]**2
				print(matriz[i][j],end=' ') #a questao n qr com espaços após o ultimo numero 
			print('')
		print('')

		teste += 1
if __name__ == '__main__':
	main()