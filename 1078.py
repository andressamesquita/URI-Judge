#-*- coding: utf-8 -*-
def main():
	contador = 0
	mult = 0
	N = int(input())
	tab = 0
	while contador < 10:
		if 2 < N < 1000:
			tab += N
			mult += 1
			contador = contador + 1
			print ("%i x %i = %i" %(mult, N, tab))
		if contador == 10:
			break

if __name__ == '__main__':
	main()