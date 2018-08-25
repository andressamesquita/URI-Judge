#-*- coding: utf-8 -*-
def main():
	X = int(input())
	Y = int(input())

	contador = 0
	numeros = []
	elemento = X + 1
	diferença = Y - X
	if X < Y:
		while contador < diferença:
			numeros.append(elemento)
			contador = contador + 1
			if contador == (Y - X):
				break
				print ("%i" %numeros)
	contador = 0
	numeros = []
	elemento = X - 1
	dif = X - Y
	if X > Y:
		while contador < dif :
			numeros.append(elemento)
			contador = contador + 1
			if contador == (X - Y):
				break
				print ("%i" %numeros)







if __name__ == '__main__':
	main()