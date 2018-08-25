#-*- coding:utf-8 -*-
def main():
	entrada = input()
	valores = entrada.split(" ")
	pedido = [int(numero) for numero in valores]
	codigo, quant = pedido
	
	if codigo == 1:
		preço = (4.00*quant)
		print ("Total: R$ %.2f" %preço)
	elif codigo == 2:
		preço = 4.50*quant
		print ("Total: R$ %.2f" %preço)
	elif codigo == 3:
		preço = 5.00*quant
		print ("Total: R$ %.2f" %preço)
	elif codigo == 4:
		preço = 2.00*quant
		print ("Total: R$ %.2f" %preço)
	elif codigo == 5:
		preço = 1.50*quant
		print ("Total: R$ %.2f" %preço)

if __name__ == '__main__':
	main()