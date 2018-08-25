def main():
	a = int(input())
	entradas = input()
	p,c,q = int(entradas.split()[0]),entradas.split()[1],int(entradas.split()[2])

	if c == '*':
		r = p * q
	else:
		r = p + q

	if r <= a:
		print('OK')
	else:
		print('OVERFLOW')

if __name__ == '__main__':
	main()