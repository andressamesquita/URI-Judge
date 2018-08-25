def main():

	name = []
	sobrenomes = []	
	while 1:
		nome = input()
		
		if nome == '0':
			break
		else:
			name.append(nome)

	for i in name:
		sobrenomes.append(i.lower())
				
	print(name)
	sobrenomes.sort()
	print(sobrenomes)


if __name__ == '__main__':
	main()