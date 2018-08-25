def main():
	entradas = input()

	t1 = int(entradas.split()[0])
	t2 = int(entradas.split()[1])
	t3 = int(entradas.split()[2])
	t4 = int(entradas.split()[3])

	qtd_aparelhos = (t1 + t2 + t3 + t4) - 3

	print ('%i'%qtd_aparelhos)

if __name__ == '__main__':
	main()