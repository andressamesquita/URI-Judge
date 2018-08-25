def main():

	lista = []
	while True:
		try:

			entrada = input()
			lista.append(entrada)

		except:
			conferindo(lista)

def conferindo(lista):
	qtd = 0
	c = 1
	diferente = True

	while diferente:
		diferente = False
		for i in range(len(lista)-c):
			if lista[i] != lista[i+1]:
				qtd += 1
				diferente = True
		c += 1

	print(qtd)

if __name__ == '__main__':
	main()