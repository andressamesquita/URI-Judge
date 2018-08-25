def main():

	n = int(input())
	quebrados = 0

	for i in range(n):
		entradas = input()
		latas,copos = [int(num) for num in entradas.split()]
		if latas > copos:
			quebrados += copos
	
	print(quebrados)

if __name__ == '__main__':
	main()