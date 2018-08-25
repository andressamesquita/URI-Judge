def main():

	entradas = input()
	hr_inicial = int(entradas.split()[0])
	minut_inicial = int(entradas.split()[1])
	hr_final = int(entradas.split()[2])
	minut_final = int(entradas.split()[3])
	minuto_dia = 1440
			
	minuto_inicial_total = (hr_inicial*60)+minut_inicial
	minuto_final_total = (hr_final*60)+minut_final

	diferenca = minuto_final_total - minuto_inicial_total
	
	if diferenca <= 0:
		diferenca += minuto_dia

	print ('O JOGO DUROU %i HORA(S) E %i MINUTO(S)' %(diferenca//60,diferenca%60))


if __name__ == '__main__':
	main()