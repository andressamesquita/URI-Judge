def main():

	palavra = input()
	tamanho = len(palavra)
	ultimo_elem = tamanho - 1

	for s in range(tamanho):
		for x in palavra:
			print(x,end=' ')
		print('')

if __name__ == '__main__':
	main()