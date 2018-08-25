def main():
	x = int(input())

	c = 1
	for i in range(x):
		entradas = input().split()
		sheldon,raj = entradas
		
		if sheldon == raj: #talvez deh erro ---> caso o console comparar endereço de memoria e nao as strings 
			print ('Caso #%i: De novo!'%c)

		elif sheldon == 'tesoura' and raj == 'papel':
			print ('Caso #%i: Bazinga!'%c)

		elif sheldon == 'papel' and raj == 'pedra':
			print ('Caso #%i: Bazinga!'%c)

		elif sheldon == 'pedra' and raj == 'lagarto':
			print('Caso #%i: Bazinga!'%c)

		elif sheldon == 'lagarto' and raj == 'Spock':
			print('Caso #%i: Bazinga!'%c)

		elif sheldon == 'Spock' and raj == 'tesoura':
			print('Caso #%i: Bazinga!'%c)

		elif sheldon == 'tesoura' and raj == 'lagarto':
			print('Caso #%i: Bazinga!'%c)

		elif sheldon == 'lagarto' and raj == 'papel':
			print('Caso #%i: Bazinga!'%c)

		elif sheldon == 'papel' and raj == 'Spock':
			print('Caso #%i: Bazinga!'%c)

		elif sheldon == 'Spock' and raj == 'pedra':
			print('Caso #%i: Bazinga!'%c)

		elif sheldon == 'pedra' and raj == 'tesoura':
			print('Caso #%i: Bazinga!'%c) 

		else:
			print('Caso #%i: Raj trapaceou!'%c)

		c += 1


if __name__ == '__main__':
	main()