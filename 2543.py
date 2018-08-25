def main():

	while True:
		try:
			entradas = input()
			qtd_gamers = int(entradas.split()[0])
			identificador = int(entradas.split()[1])

			cont = 0
			for i in range(qtd_gamers):
				entradas = input()
				ident_gamer = int(entradas.split()[0])
				game = int(entradas.split()[1])

				if ident_gamer == identificador and game == 0:
					cont += 1
			
			print (cont)

		except:
			break

if __name__ == '__main__':
	main()