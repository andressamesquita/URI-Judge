def main():
	c = int(input())
	entradas = input()
	valores = [int(i) for i in entradas.split()]

	satisfatorio = valores.count(0)
	nao_satisf = valores.count(1)
	
	if satisfatorio == nao_satisf:
		print ('N')
	
	elif satisfatorio > nao_satisf:
		print ('Y')
	else:
		print ('N')



if __name__ == '__main__':
	main()