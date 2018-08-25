def main():

	qtd = 0
	total = 0
	while True:
		try:
			nome = input()
			medida = int(input())
			qtd += 1
			total += medida
														
		except:
			print('%.1f'%(total/qtd))
			break

if __name__ == '__main__':
	main()