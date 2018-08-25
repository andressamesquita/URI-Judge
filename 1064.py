#-*- coding: utf-8 -*-
def main():
	v1 = float(input())
	v2 = float(input())
	v3 = float(input())
	v4 = float(input())
	v5 = float(input())
	v6 = float(input())
	positivos = []
	negativos = []
	if v1 > 0:
		positivos.append(v1)
	else:
		negativos.append(v1)

	if v2 > 0:
		positivos.append(v2)
	else:
		negativos.append(v2)

	if v3 > 0:
		positivos.append(v3)
	else:
		negativos.append(v3)
	if v4 > 0:
		positivos.append(v4)
	else:
		negativos.append(v4)

	if v5 > 0:
		positivos.append(v5)
	else:
		negativos.append(v5)

	if v6 > 0:
		positivos.append(v6)
	else:
		negativos.append(v6)
	
	quant_posi = len(positivos)
	if quant_posi == 1:
		n1 = positivos
		media = n1/len(positivos)
	elif quant_posi == 2:
		n1, n2 = positivos
		media = (n1 + n2)/len(positivos)
	elif quant_posi == 3:
		n1, n2, n3 = positivos
		media = (n1 + n2 + n3)/len(positivos)
	elif quant_posi == 4:
		n1, n2, n3, n4 = positivos
		media = (n1 + n2 + n3 + n4)/ len(positivos)
	elif quant_posi == 5:
		n1, n2, n3, n4, n5 = positivos
		media = (n1 + n2 + n3 + n4 + n5)/len(positivos)
	
	print ("%i valores positivos" %quant_posi)
	print ("%.1f" %media)
if __name__ == '__main__':
	main()