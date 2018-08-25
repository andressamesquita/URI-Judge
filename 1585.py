def main():
	n = int(input())
	for i in range(n):
		entradas = input()
		b,c = int(entradas.split()[0]),int(entradas.split()[1])

		area = (b*c)/2
		print ('%i cm2'%area)

if __name__ == '__main__':
	main()