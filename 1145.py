def main():

	entradas = input().split()
	qtd_num_linha = int(entradas[0])
	limite = int(entradas[1])

	
	for i in range(1,limite+1):
		if i % qtd_num_linha == 0:
			print (i)
		else:
			print (i, end = ' ')

if __name__ == '__main__':
	main()