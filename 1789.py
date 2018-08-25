def main():
	while True:
		try:

			num_lesmas = int(input())
			entradas = input()
			valores = entradas.split()
			lista = [int(i) for i in valores]
			mais_veloz = max(lista)
			
			if mais_veloz < 10:
				print ('1')
			elif 10 <= mais_veloz < 20:
				print ('2') 
			elif mais_veloz >= 20:
				print ('3')
		
		except:
			break

if __name__ == '__main__':
	main()