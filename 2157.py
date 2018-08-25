def main():
	n = int(input())

	string = ''
	sequencia = []
	for a in range(n):
		
		entradas = input()
		x,y = int(entradas.split()[0]), int(entradas.split()[1])

		sequencia = []
		for i in range(x,y+1):
			sequencia.append(i)

		for s in sequencia:
			string += str(s)

		inverso = string[::-1]
		espelho = string+inverso 
		
		print (espelho)
		inverso = ''
		string = ''
		espelho = ''
			
		
if __name__ == '__main__':
	main()