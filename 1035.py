#-*- coding:utf-8 -*-
def main():
	entrada = input()
	valores_str = entrada.split(" ")
	numeros = [int(numero) for numero in valores_str]
	A, B, C, D = numeros

	if (B>C) and (D>A) and (C+D)>(A+B) and (C>0) and (D>0) and A/2:
		print ("Valores aceitos")
	else:
		print ("Valores nao aceitos")
if __name__ == '__main__':
	main()