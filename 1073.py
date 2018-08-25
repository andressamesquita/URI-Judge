#-*- coding: utf-8 -*-
def main():
	N = int(input())
	if 2 < N < 2000:
		numeros = N - 1
		while numeros < N:
			if numeros % 2 == 0:
				quadrado = numeros * 2
				numeros = numeros - 1
				print ("%i^2 = %i" %(numeros, quadrado))
			if numeros == 0:
				break

if __name__ == '__main__':
	main()
