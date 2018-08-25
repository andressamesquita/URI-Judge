#-*- coding: utf-8 -*-
def main():
	entrada = input()
	lados = entrada.split(" ")
	valores = [float(lado) for lado in lados]
	A, B, C = valores
	if (abs(B-C) < A < B + C) or (abs(A-C) < B < A+C) or (abs(A-B) < C < A + B):
		perimetro = A + B + C
		print ("Perimetro = %.1f" %perimetro)
	else:
		trapezio = ((A + B)*C)/2
		print ("Area = %.1f" %trapezio)
if __name__ == '__main__':
 	main() 