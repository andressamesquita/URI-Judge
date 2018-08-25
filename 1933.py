def main():
	entradas = input()
	n1 = int(entradas.split()[0])
	n2 = int(entradas.split()[1])

	if n1 > n2:
		print ('%i' %n1)

	elif n1 < n2:
		print ('%i' %n2)
	
	else:
		print ('%i' %n2)

if __name__ == '__main__':
	main()