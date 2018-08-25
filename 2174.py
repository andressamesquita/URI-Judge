def main():

	n = int(input())

	pokemons = []
	for i in range(n):
		pokemon = input()
		pokemons.append(pokemon.upper())

	contagem = []
	for i in pokemons:
		if i not in contagem:
			contagem.append(i)

	faltam = 151-len(contagem)

	print ('Falta(m) %i pomekon(s).'%faltam)

if __name__ == '__main__':
	main()