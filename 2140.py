def main():
	
	entradas = 0
	valor_prod = 0
	pagamento = 0

	while True:

		entradas = input()
		valor_prod = int(entradas.split()[0])
		pagamento = int(entradas.split()[1])

		if valor_prod == pagamento == 0:
			break

		troco = pagamento - valor_prod

		if troco > 150 or pagamento/valor_prod == 2:
			print ('impossible')
		elif troco <= 150:
			if troco / 100 == 2 or troco / 50 == 2 or troco / 20 == 2 or troco / 10 == 2 or troco / 5 == 2:
				print ('possible')
		
		

if __name__ == '__main__':
	main()