def main():

	while True:
		try:

			entradas = input()
			A,B,C = int(entradas.split()[0]), int(entradas.split()[1]), int(entradas.split()[2])

			if A == B and A != C:
				print ('C')
			elif A == C and A != B:
				print ('B')
			elif B == C and B != A:
				print ('A')
			else:
				print ('*')
		
		except:
			break

if __name__ == '__main__':
	main()