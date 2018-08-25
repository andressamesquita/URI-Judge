def main():

	while True:
		try:

			dna = input()
			resistencia = input()

			if resistencia in dna:
				print('Resistente')
			
			else:
				print('Nao resistente')

		except:
			break
			
if __name__ == '__main__':
	main()