#-*- coding: utf-8 -*-
def main():
	N = int(input())
	contador = 0
	while 1 <= N <= 20:
		X = int(input())
		contador = contador + 1
		if (1 <= X <= (10**8)) and (X % 2 == 0) and (X!=2):
			print ("%i eh perfeito" %X)
		elif (1 <= X <= (10**8)) and (X % 2 != 0) and (X!=2):
			print ("%i nao eh perfeito" %X)
		elif (X == 2):
			print ("%i nao eh perfeito" %X)
		elif (X == 3):
			print ("%i nao eh perfeito" %X)
		if contador == N:
			break

if __name__ == '__main__':
	main()