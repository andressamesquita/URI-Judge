def main():

	while True:
		
		entradas = input()
		l,r = int(entradas.split()[0]), int(entradas.split()[1])
		
		if l == r == 0:
			break
		else:
			soma = l + r
			print (int(soma))


if __name__ == '__main__':
	main()