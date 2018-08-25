def main():
	testes = int(input())

	for i in range(1,testes+1):
		numero = int(input())
		
		primo = 0
		for i in range(1,numero+1):
			if numero % i == 0:
				primo +=1

		if primo > 2:
			print ('Not Prime')
		else:
			print ('Prime')


if __name__ == '__main__':
	main()