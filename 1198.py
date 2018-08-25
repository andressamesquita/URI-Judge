def main():

	while True:
		try:

			entradas = input()
			s1 = int(entradas.split()[0])
			oponente = int(entradas.split()[1])
		
			if oponente > s1:
				dif = oponente - s1
				print ('%i'%dif)

			else:
				dif = s1 - oponente 
				print ('%i'%dif)

		except:
			break
	
	

if __name__ == '__main__':
	main()