#-*- coding: utf-8 -*-
from math import sqrt
def main():
	entrada = input()
	valores = entrada.split(" ")
	numeros = [float(numero) for numero in valores]
	A, B, C = numeros

	delta = (B**2) - (4*A*C)
	if delta < 0:
		print ("Impossivel calcular")
	if delta >= 0:
		R1 = (-B + sqrt(delta)) / 2*A
		R2 = (-B - sqrt(delta)) / 2*A
		print ("R1 = %.5f" %R1)
		print ("R2 = %.5f" %R2) 

if __name__ == '__main__':
	main()