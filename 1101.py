#-*- coding: utf-8 -*-
def main():
	M = None
	N = None
	while True:
		entrada = input()
		numeros = entrada.split(" ")
		valores = [int(numero) for numero in numeros]
		M, N = valores
		if M <= 0 or N <= 0:
			break
	
	

if __name__ == '__main__':
	main()