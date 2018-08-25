def main():

	entradas = input()
	sensor,limite = int(entradas.split()[0]),int(entradas.split()[1])

	qtd = 0
	c = 0
	for i in range(sensor):
		entradas = input()
		exit,enter = int(entradas.split()[0]),int(entradas.split()[1])
		qtd -= exit
		qtd += enter 
		
		
		if qtd > limite:
			c = 1
		
	if c == 0:
		print('N')
	else:
		print('S')


if __name__ == '__main__':
	main()