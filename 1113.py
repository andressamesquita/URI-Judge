#-*-coding: utf-8-*-
def main():
	X = None
	Y = None
	while True:
		entrada = input()
		numeros = entrada.split(" ")
		valores = [int(numero) for numero in numeros]
		X, Y = valores
		if X > Y:
			print ("Decrescente")
		elif X < Y:
			print ("Crescente")
		if X == Y:
			break

if __name__ == '__main__':
	main()