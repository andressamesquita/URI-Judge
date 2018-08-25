def main():
	while True:
		try:

			lista = []
			entradas = input()
			qtd, numero = int(entradas.split()[0]),entradas.split()[1]

			lista += numero

			soma = 0
			for i in lista:
				soma += int(i) 
			
			if soma % 3 == 0:
				print ('%i sim'%soma)
			else:
				print ('%i nao'%soma)

		except:
			break

if __name__ == '__main__':
	main()