def main():

	entradas = input()
	otavio,bruno,ian = [float(a) for a in entradas.split()]

	if otavio == bruno == ian or otavio == bruno or otavio == ian or ian == bruno:
		print('Empate')

	elif otavio < bruno and otavio < ian:
		print('Otavio')

	elif bruno < otavio and bruno < ian:
		print('Bruno')
	else:
		print('Ian')

if __name__ == '__main__':
	main()