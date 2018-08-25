def main():
	#python2
	n = int(input())
	teste = 4
	for i in range(n):
		m = int(input())
	
		
		matriz = []
		for j in range(m):
			entradas = raw_input()
			coluna = [int(i) for i in entradas.split()]
			matriz.append(coluna)

				
		print('Quadrado da matriz #%i:'%teste)
		for i in range(len(matriz)):
			for j in range(len(matriz[i])):
				matriz[i][j] = matriz[i][j]**2
				print(matriz[i][j]), #a questao n qr com espaços após o ultimo numero ACHO
			print('')
		print('')

		teste += 1
if __name__ == '__main__':
	main()