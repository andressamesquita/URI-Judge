def main():

	while True:
		n = int(input())
		if n == 0:
			break
		else:
			valores = input().split()
			maria = valores.count('0')
			joao = valores.count('1')

			print('Mary won %i times and John won %i times' %(maria,joao))

if __name__ == '__main__':
	main()