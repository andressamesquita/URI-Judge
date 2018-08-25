def main():
	entradas = input()
	atual,aumentado = float(entradas.split()[0]),float(entradas.split()[1])

	percent = ((aumentado*100)/atual)-100


	print('%.2f%%'%percent)

if __name__ == '__main__':
	main()