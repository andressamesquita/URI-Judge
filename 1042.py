#-*- coding: utf-8 -*-
def main():
	entrada = input()
	numeros = entrada.split(" ")
	valores = [int(numero) for numero in numeros]
	valor_1, valor_2, valor_3 = valores
	if valor_1 < valor_2 < valor_3:
		print("%i" %valor_1)
		print("%i" %valor_2)
		print("%i" %valor_3)
	elif valor_1 < valor_3 < valor_2:
		print("%i" %valor_1)
		print("%i" %valor_3)
		print("%i" %valor_2)
	elif valor_2 < valor_3 < valor_1:
		print("%i" %valor_2)
		print("%i" %valor_3)
		print("%i" %valor_1)
	elif valor_2 < valor_1 < valor_3:
		print("%i" %valor_2)
		print("%i" %valor_1)
		print("%i" %valor_3)
	elif valor_3 < valor_2 < valor_1:
		print("%i" %valor_3)
		print("%i" %valor_2)
		print("%i" %valor_1)
	elif valor_3 < valor_1 < valor_2:
		print("%i" %valor_3)
		print("%i" %valor_1)
		print("%i \n" %valor_2)
	print("\n%i" %valor_1)
	print("%i" %valor_2)
	print("%i" %valor_3)
if __name__ == '__main__':
	main()