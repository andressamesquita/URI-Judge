def main():

	n = int(input())

	for k in range(n):
		a = int(input())
		entradas = input()
		c,d,e,f = [int(k) for k in entradas.split()]
		b = int(input())

		if a + b == 7 and c + e == 7 and d + f == 7:
			print('SIM')
			
		else:
			print('NAO')

if __name__ == '__main__':
	main()