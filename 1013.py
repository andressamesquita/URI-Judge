#-*- coding: utf-8 -*-
def main():
	entrada = input()
	valores_string = entrada.split(" ")
	numeros = [int(valor) for valor in valores_string]
	a, b, s = numeros

	if a > b > s:
		maior_AB = ((a+b+(a*b*s))*(a-b))/2
		print ("%i eh o maior" %a)
	elif b > a > s:
		maior_AB = ((a+b+(a*b*s))*(a-b))/2
		print ("%i eh o maior" %b)
	elif s > b > a:
		maior_AB = ((a+b+(a*b*s))*(a-b))/2
		print ("%i eh maior" %s)

if __name__ == '__main__':
	main()