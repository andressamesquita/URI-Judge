def main():
	n = int(input())
	entradas_1 = input()
	entradas_2 = input()
	
	LA,LB = [int(i) for i in entradas_1.split()]
	SA,SB = [int(i) for i in entradas_2.split()]

	if n >= LA and n <= LB and n >= SA and n <= SB:
		print('possivel')
	else:
		print('impossivel')

if __name__ == '__main__':
	main()