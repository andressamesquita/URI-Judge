def main():
	entradas = input()
	a, b, c = entradas.split()

	if a > b and b <= c:
		print (':)')

	if b > a and c <= b:
		print (':(')

	if b > a and c > b and c-b < b-a :
		print (':(')

	if b > a and c > b and c-b >= b-a:
		print (':)')

	if b < a and c < b and b-c < a-b:
		print (':)')

	if a > b and b > c and b-c <= a-b:
		print (':(')
	#talvez um 'if' por fora caso deh erro
	elif b == a and c > b:
		print (':)')
	else:
		print (':(')


if __name__ == '__main__':
	main()