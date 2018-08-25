def main():

	numero = input()
	frequencia = []

	for i in numero:
		qtd = numero.count(i)
		frequencia.append(qtd)

	mais_frequente = numero[frequencia.index(max(frequencia))]
	print(mais_frequente)

	c = 0
	n = frequencia[c]
	for j in range(len(frequencia)):
		if j == n:
			mais_frequente = numero[frequencia[j]]





if __name__ == '__main__':
	main()