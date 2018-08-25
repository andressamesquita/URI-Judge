def main():
	n = int(input())

	for i in range(n):
		nome = input()
		
		if len(nome) == 5:
			print('3')

		else:
			if nome[0] == 'o' and nome[1] == 'n' or nome[2] == 'e' and nome[0] == 'o' or nome[2] == 'e' and nome[1] == 'n':
				print('1')
			else:
				print('2')


if __name__ == '__main__':
	main()