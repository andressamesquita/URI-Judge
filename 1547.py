def main():

	n = int(input())

	for i in range(n):
		entradas_1 = input()
		entradas_2 = input()

		qtd_alunos,adivinha = [int(i) for i in entradas_1.split()]
		valores = [int(a) for a in entradas_2.split()]


		for x in valores:
			if x == adivinha:
				posicao = valores.index(x)+1
				print('%i'%posicao)
				break

			elif x == adivinha + 1:
				posicao = valores.index(x)+1
				print('%i'%posicao)
				break
			
			elif x == adivinha - 1:
				posicao = valores.index(x)+1
				print('%i'%posicao)
				break
		



if __name__ == '__main__':
	main()