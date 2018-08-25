def main():

	n = int(input())

	
	for i in range(n):
		entradas = input()
		tamanho_avenida,radar = [int(k) for k in entradas.split()]
		a = radar
		c = 1
		while a < tamanho_avenida:
			a += radar
			c += 1
			if a >= tamanho_avenida:
				break

		print(c)

if __name__ == '__main__':
	main()