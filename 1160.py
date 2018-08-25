def main():
	n = int(input())

	for i in range(n):
		entradas = input()
		PA,PB,percA,percB = [float(num) for num in entradas.split()]

		qtd = 0
		while PA <= PB:
		
			qtd += 1
			PA += int(PA*float(percA/100))
			PB += int(PB*float(percB/100))
			if qtd > 100:
				break

		if qtd > 100:
			print('Mais de 1 seculo.')
		else:
			print('%i anos.'%qtd)


if __name__ == '__main__':
	main()