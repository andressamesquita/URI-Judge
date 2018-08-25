def main():

	letra = input()
	entradas = input()
	palavras = [i for i in entradas.split()]

	cont = 0
	for i in palavras:
		if letra in i:
			cont += 1

	media = (cont/len(palavras))*100

	print('%.1f'%media)


if __name__ == '__main__':
	main()