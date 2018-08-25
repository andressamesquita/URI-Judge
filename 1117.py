#-*- coding: utf-8 -*-
def main():
	numeros = []
	while True:
		nota = float(input())
		if nota < 0:
			print ("nota invalida")
		if 0 <= nota <= 10:
			numeros.append(nota)
			"""contador = contador + 1
			notas = [nota for nota in valores]
			nota_1, nota_2 = notas
			media = (nota_1 + nota_2)/2
			print ("media = %.2f" %media)
			if contador == 2:
				break"""
		if len(numeros) == 2:
			break
			print ("%f" %numeros)
if __name__ == '__main__':
	main()