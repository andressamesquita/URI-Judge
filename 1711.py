def main():

	n = int(input())

	vetor = []
	for i in range(n):
		numero = int(input())
		vetor.append(numero)

	print(vetor)
	
	ordem = vetor.sort()
	
	qtd_na_ordem = [] 
	for j in range(len(ordem)):
		qtd = vetor.count(vetor[j])
		qtd_na_ordem.append(qtd)

	print(qtd_na_ordem)






if __name__ == '__main__':
	main()