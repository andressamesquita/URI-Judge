def main():

	n = int(input())

	for i in range(n):
		qtd = int(input())

		if qtd % 2 == 0:
			print ('0')
		else:
			print ('1')

if __name__ == '__main__':
	main()