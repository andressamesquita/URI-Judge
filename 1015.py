#-*- coding: utf-8 -*-
from math import sqrt
def main():
	entrada_1 = input()
	entrada_2 = input()

	valores_1 = entrada_1.split(" ")
	numeros1 = [float(numero) for numero in valores_1]
	x1, y1 = numeros1

	valores_2 = entrada_2.split(" ")
	numeros2 = [float(numero) for numero in valores_2]
	x2, y2 = numeros2

	DISTANCIA = sqrt(((x2 - x1)**2)+((y2 - y1)**2))

	print ("%.4f" %DISTANCIA)
if __name__ == '__main__':
	main()