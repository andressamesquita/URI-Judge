def main():
	while True:

		entradas = input()
		m = int(entradas.split()[0])
		n = int(entradas.split()[1])

		if m == n == 0:
			break
		else:
			soma = m + n 
		
			numero = str(soma)
			numero = numero.replace('0','')

			print (numero)


if __name__ == '__main__':
	main()