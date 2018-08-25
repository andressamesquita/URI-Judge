def main():

	while 1:

		n = int(input())
		
		if n == 0:
			break
		
		else:

			p = []
			vetor = []
			for i in range(n):
				entrada = input()
				planeta,ano,demora = entrada.split()[0],int(entrada.split()[1]),int(entrada.split()[2])
				p.append(planeta)
				
				diferenca = ano - demora
				vetor.append(diferenca)
				indice = vetor.index(min(vetor))

			print(p[indice]) 


if __name__ == '__main__':
	main()