def main():
	qtd = int(input())

	lista = []
	
	for i in range(qtd):
		nome = input()
		dif = float(input())

		notas = input()
		valores = notas.split()
		lista = [float(i) for i in valores]
		

		lista.sort()
		
		maximo = len(lista)-1
		

		del lista[maximo]
		
		del lista[0]
				
		resultado = sum(lista)*dif
		print('%s %.2f'%(nome,resultado))

if __name__ == '__main__':
	main()