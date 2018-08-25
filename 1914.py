def main():
	x = int(input())

	for i in range(x):
		entradas = input()
		jog_1 = entradas.split()[0]
		esc_1 = entradas.split()[1]
		jog_2 = entradas.split()[2]
		esc_2 = entradas.split()[3]

		valores = input()
		n = int(valores.split()[0])
		m = int(valores.split()[1])

		soma = n + m
		if soma % 2 == 0:
			soma = 'PAR'
			if esc_1 == soma:
				print (jog_1)
			else:
				print (jog_2)
		else:
			soma = 'IMPAR'
			if esc_1 == soma:
				print (jog_1)
			else:
				print (jog_2)
				
if __name__ == '__main__':
	main()