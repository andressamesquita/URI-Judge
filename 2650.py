def main():
	entradas = input()
	n,t1 = [int(k) for k in entradas.split()]

	maiores = []
	for i in range(n):
		maiores.append([])
		entradas = input()
		maiores[i] += entradas.split()

		lista = []
		for i in range(len(maiores)):
			if int(maiores[i][2]) > t1:
				lista.append(i)
	
	print(lista)
if __name__ == '__main__':
	main()