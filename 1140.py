def main():

	while True:

		entrada = input()
		
		if entrada == '*':
			break

		else:

			lista = entrada.split()
			tautograma = 0
			comparar = []
				
			for elemento in lista:
				comparar.append(elemento.upper()) 
			
			tamanho = len(comparar)
			ultimo_elem = tamanho-1
			
			letras = []
			
			for elemento in range(len(comparar)):
				letras.append(comparar[elemento][0])
				

			tam = len(letras)-1
			iguais = 0
			for item in letras:
				for itens in letras:
					if itens != item:
						iguais = 1
						break

			if iguais == 1:
				print ('N')
			else:
				print ('Y')
			

if __name__ == '__main__':
	main()