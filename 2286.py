def main():

	teste = 0
	while True:

		n = int(input())

		if n == 0:
			break
		else:
			teste += 1
			p1_par = input()
			p2_impar = input()

			print('Teste %i'%teste)
			for num in range(n):
				entradas = input()
				L = [int(i) for i in entradas.split()]
				
				if sum(L) % 2 == 0:
					print(p1_par)
				else:
					print(p2_impar)
			print('')

if __name__ == '__main__':
	main()