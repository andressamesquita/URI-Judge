def main():
	while True:
		n = int(input())

		if n == 0:
			break 
	
		else:

			pontos_a = 0
			pontos_b = 0
			for t in range(n):
				valores = input()
				a,b = int(valores.split()[0]),int(valores.split()[1])

				if a == b:
					continue
				elif a > b:
					pontos_a += 1
				else:
					pontos_b += 1
					
			print('%i %i'%(pontos_a,pontos_b))



if __name__ == '__main__':
	main()