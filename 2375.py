def main():

	diametro = int(input())
	entradas = input()
	valores = [int(i) for i in entradas.split()]

	a = -1
	for i in valores:
		if i < diametro:
			a = -1
			print('N')
			break
		else:
			a = 1

	if a == 1:
		print ('S')
	
if __name__ == '__main__':
	main()