def main():
	N = int(input())

	total = 0
	sapo = 0
	coelho = 0
	rato = 0
	for i in list(range(1,N+1)):
		entradas = input()
		qtd = int(entradas.split()[0])
		cobaia = str(entradas.split()[1])

		if 1 <= qtd <= 15:
			total += qtd
			if cobaia == 'S':
				sapo += qtd
			elif cobaia == 'C':
				coelho += qtd
			elif cobaia == 'R':
				rato += qtd

	percent_coelho = (coelho/total)*100
	percent_sapo = (sapo/total)*100
	percent_rato = (rato/total)*100

	print ('Total: %i cobaias' %total)
	print ('Total de coelhos: %i' %coelho)
	print ('Total de ratos: %i' %rato)
	print ('Total de sapos: %i' %sapo)
	print ('Percentual de coelhos: %.2f %%' %percent_coelho)
	print ('Percentual de ratos: %.2f %%' %percent_rato)
	print ('Percentual de sapos: %.2f %%' %percent_sapo)
		
if __name__ == '__main__':
	main()