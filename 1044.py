#-*- coding: utf-8 -*-
def main():
	entrada = input()
	valores = entrada.split(" ")
	numeros = [int(algarismo) for algarismo in valores]
	A, B = numeros
	if A % B == 0 or B % A == 0:
		print ("Sao Multiplos") 
	else:
		print ("Nao sao Multiplos")
if __name__ == '__main__':
	main()