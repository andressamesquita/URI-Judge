def main():

	while 1:
		n = int(input())
		if n == 0:
			break
		else:
			entradas = input()
			valores = [int(i) for i in entradas.split()]
			ordem = sorted(valores)
			
			segundo_maior = ordem[len(valores)-2]
			
			indice = valores.index(segundo_maior)
			print(indice+1)

if __name__ == '__main__':
	main()