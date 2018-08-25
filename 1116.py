#-*- coding: utf-8 -*-
def main():
	N = int(input())
	contador = 0
	divisao = 0
	while contador <= N:
		entrada = input()
		valores = entrada.split(" ")
		numeros = [int(numero) for numero in valores]
		X, Y = numeros
		contador = contador + 1
		if X < 0:
			print ("divisao impossivel")
		elif X < Y:
			divisao = X / Y
			print ("%.1f" %divisao)
		elif Y == 0:
			divisao = X
			print ("%.1f" %divisao)
		elif X == 0:
			divisao = 0
			print ("%.1f" %divisao)
		elif X > Y:
			divisao = X / Y
			print ("%.1f" %divisao)
		elif X == Y != 0:
			divisao = 1
			print ("%.1f" %divisao)
		elif X == 0 and Y == 0:
			divisao = 0
			print ("%.1f" %divisao)
		else:
			print ("divisao impossivel")
		if contador == N:
			print ("\n")
			break	 
if __name__ == '__main__':
	main()