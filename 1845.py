def main():
	while True:
		try:

			texto = input()

			new = ''
			for i in texto:
				if i == 's' or i == 'j' or i == 'b' or i == 'z' or i == 'p' or i == 'v' or i == 'x':
					i = 'f'
				if i == 'S' or i == 'J' or i == 'B' or i == 'Z' or i == 'P' or i == 'V' or i == 'X':
					i = 'F'
				new += i

			correta = new.replace('ff','f')
			correta = new.replace('Ff','F')
			correta = new.replace('fF','f')
			correta = new.replace('FF','F')

			print(correta)
		except:
			break

if __name__ == '__main__':
	main()