def main():
	b = input()

	qtd_um = 0
	qtd_zero = 0
	for i in b:
		if i == '1':
			qtd_um += 1
		else:
			qtd_zero += 1

	if qtd_um % 2 == 0:
		b += '0'
		print ('%s'%b)
	else:
		b += '1'
		print ('%s'%b)






if __name__ == '__main__':
	main()