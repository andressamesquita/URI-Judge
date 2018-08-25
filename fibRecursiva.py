def main():
	n = int(input( 'digite um n: ' ))
	print (fibonacci(0,1,n))

def fibonacci(n1,n2,n):
	if n1 == 0:
		print (n1,n2, end=' ')
	atual = n1 + n2
	if atual > n:
		print('fim')
	else:
		print (atual, end=' ')
		n1 = n2
		n2 = atual
		return fibonacci(n1,n2,n) 

	
if __name__ == '__main__':
	main()