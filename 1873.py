def main():
	x = int(input())

	
	for i in range(x):
		entradas = input().split()
		raj,sheldon = entradas
		
		if sheldon == raj: 
			print ('empate')

		elif sheldon == 'tesoura' and raj == 'papel':
			print ('sheldon')

		elif sheldon == 'papel' and raj == 'pedra':
			print ('sheldon')

		elif sheldon == 'pedra' and raj == 'lagarto':
			print('sheldon')

		elif sheldon == 'lagarto' and raj == 'spock':
			print('sheldon')

		elif sheldon == 'spock' and raj == 'tesoura':
			print('sheldon')

		elif sheldon == 'tesoura' and raj == 'lagarto':
			print('sheldon')

		elif sheldon == 'lagarto' and raj == 'papel':
			print('sheldon')

		elif sheldon == 'papel' and raj == 'spock':
			print('sheldon')

		elif sheldon == 'spock' and raj == 'pedra':
			print('sheldon')

		elif sheldon == 'pedra' and raj == 'tesoura':
			print('sheldon') 

		else:
			print('rajesh')

		


if __name__ == '__main__':
	main()