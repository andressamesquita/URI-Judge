def main():
	while True:
		try:

			entradas = input()
			qtd,minima,maxima = int(entradas.split()[0]),int(entradas.split()[1]),int(entradas.split()[2])
			
			lista = []
			for a in range(qtd):
				alturas = int(input())
				if alturas >= minima and alturas <= maxima:
					lista.append(alturas)

			print (len(lista))

		except:
			break

if __name__ == '__main__':
	main()