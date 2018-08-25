from math import sqrt
def main():
	while True:
		try:
			n = int(input())
			entradas = input()
			h,c,l = [int(i) for i in entradas.split()]

			x = sqrt((c**2)+(h**2))

			base = x*n

			area = (base * l)/10000
			print('%.4f'%area)

		except:
			break
if __name__ == '__main__':
	main()