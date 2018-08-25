#-*- coding: utf-8 -*-
def main():
	v1 = int(input())
	v2 = int(input())
	v3 = int(input())
	v4 = int(input())
	v5 = int(input())
	pares = []
	impares = []
	positivos = []
	negativos = []

	if v1 % 2 == 0:
		pares.append(v1)
	else:
		impares.append(v1)
	if v1 > 0 :
		positivos.append(v1)
	elif v1 < 0:
		negativos.append(v1)
	if v2 % 2 == 0:
		pares.append(v2)
	else:
		impares.append(v2)
	if v2 > 0 :
		positivos.append(v2)
	elif v2 < 0:
		negativos.append(v2)
	if v3 % 2 == 0:
		pares.append(v3)
	else:
		impares.append(v3)
	if v3 > 0:
		positivos.append(v3)
	elif v3 < 0:
		negativos.append(v3)
	if v4 % 2 == 0:
		pares.append(v4)
	else:
		impares.append(v4)
	if v4 > 0:
		positivos.append(v4)
	elif v4 < 0:
		negativos.append(v4)
	if v5 % 2 == 0:
		pares.append(v5)
	else:
		impares.append(v5)
	if v5 > 0:
		positivos.append(v5)
	elif v5 < 0:
		negativos.append(v5)
	quant_pares = len(pares)
	quant_imp = len(impares)
	quant_posit = len(positivos)
	quant_neg = len(negativos)
	print ("%i valor(es) par(es)" %quant_pares)
	print ("%i valor(es) impar(es)" %quant_imp)
	print ("%i valor(es) positivo(s)" %quant_posit)
	print ("%i valor(es) negativo(s)" %quant_neg)

if __name__ == '__main__':
	main()