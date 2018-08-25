def main():
	 
	while True:
		X = int(input())

		if X == 0:
			break

		else:
			soma = 0
			for i in range(X,X+10):
				if X % 2 == 0:
					soma += X
					X += 1
					
				else:
					X += 1
			
			print ('%i'%soma)

if __name__ == '__main__':
	main()