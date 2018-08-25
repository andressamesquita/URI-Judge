def main():

	while 1:
		entradas = input()
		
		if entradas == '0 0 0 0':
			break
		
		else:
			l,c,r1,r2 = [int(i) for i in entradas.split()]

			area_ret = l * c

			cilindro1 = 3.14159 * (r1**2)
			cilindro2 = 3.14159 * (r2**2)

			if  area_ret >= int(cilindro1 + cilindro2):
				print('S')
			else:
				print('N')


if __name__ == '__main__':
	main()