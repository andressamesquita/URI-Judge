def main():

	soma_a = []
	soma_b = []
	adicao_a = 0
	adicao_b = 0
	new = []
	novo = []
	while True:
		entradas = input()
		a,b = entradas.split()[0],entradas.split()[1]
		
		if a == b == 0:
			break

		else:
			soma_a += a
			soma_b += b

			for i in soma_a:
				adicao_a += int(i)
				
				if adicao_a > 9:
					new += str(adicao_a)
					adicao_a = 0
					
					for k in new:
						adicao_a += int(k)
				
				else:
					continue

			for j in soma_b:
				adicao_b += int(j)
				
				if adicao_b > 9:
					novo += str(adicao_b)
					adicao_b = 0
					
					for y in novo:
						adicao_b += int(y)
				
				else:
					continue

			if adicao_a == adicao_b:
				print ('0') 
			if adicao_a > adicao_b:
				print ('1')
			else:
				print ('2')

if __name__ == '__main__':
	main()