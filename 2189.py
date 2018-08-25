def main():

	test = 0
	while True:

		n = int(input())
		
		if n == 0:
			break
		else:

			entradas = input()
			lista = [int(i) for i in entradas.split()]
			test += 1
			for i in range(len(lista)):
				if i+1 == lista[i]:
					print ('Teste %i'%test)
					print (lista[i])
					print ('')

if __name__ == '__main__':
	main()