def main():
	
	n = int(input())
	total = 0
	for i in range(1,n+1):
		entradas = input()
		codigo = entradas.split()[0]
		qtd = int(entradas.split()[1])

		if codigo == '1001':
			valor = qtd * 1.50

		elif codigo == '1002':
			valor = qtd * 2.50

		elif codigo == '1003':
			valor = qtd * 3.50

		elif codigo == '1004':
			valor = qtd * 4.50

		elif codigo == '1005':
			valor = qtd * 5.50

		total += valor

	print ('%.2f'%total)


if __name__ == '__main__':
	main()