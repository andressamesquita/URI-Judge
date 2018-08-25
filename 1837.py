def main():
	entradas = input().split()
	n1,n2 = entradas

	
	#q = (a-r)/b


	quociente = int(n1)//int(n2)
	resto = int(n1)%int(n2)
	print('%i %i'%(quociente,resto))

if __name__ == '__main__':
	main()