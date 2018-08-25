def main():

	entradas = input()
	a,b = [int(i) for i in entradas.split()]

	if a == 1 and b == 0:
		print ('B')
	elif a == 1 and b == 1:
		print ('A')
	else:
		print ('C')

if __name__ == '__main__':
	main()