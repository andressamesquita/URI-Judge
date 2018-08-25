#-*- coding: utf_8 -*-
def main():
	valor1 = int(input())
	valor2 = int(input())
	valor3 = int(input())
	valor4 = int(input())
	valor5 = int(input())
	pares = []
	n_par = []
	if valor1%2 == 0:
		pares.append(valor1)
	else:
		n_par.append(valor1)
	if valor2%2 == 0:
		pares.append(valor2)
	else:
		n_par.append(valor2)
	if valor3%2 == 0:
		pares.append(valor3)
	else:
		n_par.append(valor3)
	if valor4%2 == 0:
		pares.append(valor4)
	else:
		n_par.append(valor4)
	if valor5%2 == 0:
		pares.append(valor5)
	else:
		n_par.append(valor5)
	quant = len(pares)
	print ("%i valores pares" %quant)

if __name__ == '__main__':
	main()