#-*-coding: utf-8-*-
def main():
	entrada = input()
	valores_string = entrada.split(" ")
	numeros = [float(numero) for numero in valores_string]
	A, B, C = numeros

	area_triangulo = (A*C)/2
	area_circ = 3.14159*(C**2)
	area_trapezio = ((A + B)*C)/2
	area_quad = B**2
	area_retang = A*B

	print ("TRIANGULO: %.3f" %area_triangulo)
	print ("CIRCULO: %.3f" %area_circ)
	print ("TRAPEZIO: %.3f" %area_trapezio)
	print ("QUADRADO: %.3f" %area_quad)
	print ("RETANGULO: %.3f" %area_retang)

if __name__ == '__main__':
	main()