def main():

	matriz = [[j for j in range(1,10) if j % 2 == 0] for i in range(4)]

	print('Matriz:',matriz)


if __name__ == '__main__':
	main()