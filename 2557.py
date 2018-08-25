def main():
	while True:
		try:

			equacao = input()
			r,b = equacao.split('+')
			l,j = b.split('=')
			
			#r+l=j

			if r =='R':
				icognita = int(j) - int(l)
			elif l == 'L':
				icognita = int(j) - int(r)
			elif j == 'J':
				icognita = int(r) + int(l)
			print(icognita)

		except:
			break


if __name__ == '__main__':
	main()