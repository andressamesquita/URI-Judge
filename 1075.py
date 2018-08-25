#-*- coding: utf-8 -*-
def main():
	N = int(input())
	for numero in list(range(2, 10000)):
		if numero % N == 2:
			print (numero)

if __name__ == '__main__':
	main()