#-*- coding: utf-8 -*-
def main():
	valor = float(input())
	if 0 <= valor <= 25.0000:
		print ("Intervalo [0,25]")
	elif 25.0000 <= valor <= 50.0000000:
		print ("Intervalo (25,50]")
	elif 50.0000000 <= valor <= 75.0000000:
		print ("Intervalo (50,75]")
	elif 75.0000000 <= valor <= 100.0000000:
		print ("Intervalo (75,100]")
	else:
		print ("Fora de intervalo")
if __name__ == '__main__':
	main()