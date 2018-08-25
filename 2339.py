def main():

	a = input()
	qtd_comp,folhas,qtd_p_cada = [int(i) for i in a.split()]

	if folhas / qtd_p_cada == qtd_comp or folhas / qtd_p_cada > qtd_comp:
		print('S')
	else:
		print('N')

if __name__ == '__main__':
	main()