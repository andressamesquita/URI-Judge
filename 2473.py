def main():

	entradas_1 = input()
	entradas_2 = input()

	aposta = [int(i) for i in entradas_1.split()]
	lota = [int(j) for j in entradas_2.split()]

	qtd = 0
	for i in aposta:
		for j in lota:
			if i == j:
				qtd += 1

	if qtd < 3:
		print('azar')

	elif qtd == 3:
		print('terno')

	elif qtd == 4:
		print('quadra')

	elif qtd == 5:
		print('quina')

	elif qtd == 6:
		print('sena')

if __name__ == '__main__':
	main()