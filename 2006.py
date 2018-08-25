def main():
	cha = int(input())

	entradas = input()
	valores = entradas.split()
	lista = [int(i) for i in valores]

	qtd = 0
	for i in lista:
		if i == cha:
			qtd += 1

	print ('%i'%qtd)

if __name__ == '__main__':
	main()