def main():
	
	while 1:
		try:
			n = int(input())

			numeros = []

			for i in range(n):
				num = input()
				numeros.append(num)
			
			numeros.sort()
			[print(i) for i in numeros]

		except:
			break
if __name__ == '__main__':
	main()