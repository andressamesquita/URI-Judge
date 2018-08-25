def main():
	
	entradas = input()
	A = int(entradas.split()[0])
	B = int(entradas.split()[1])
	soma = sum([int(i) for i in range(A,B+1)])
	print (soma)

if __name__ == '__main__':
	main()