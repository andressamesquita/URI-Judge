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
	print ("%i valores positivos" %quant_posi)
if __name__ == '__main__':
	main()