def main():

	
	while 1:
	
		entradas = input()
	
		if entradas == '0 0 0':
			print('\nAqui nois constroi fibra rapaz! Nao e agua com musculo!')
			break
		else:
			esquerdo,direito,repeticoes = [int(k) for k in entradas.split()]

			calculo1 = esquerdo*(1+(repeticoes/30))
			calculo2 = direito*(1+(repeticoes/30))

			media = (calculo1+calculo2)/2
			
			if media >= 1 and media < 13:
				print('Nao vai da nao')
			elif media >= 13 and media < 14:
				print('E 13')
			elif media >= 14 and media < 40:
				print('Bora, hora do show! BIIR!')
			elif media >= 40 and media <= 60:
				print('Ta saindo da jaula o monstro!')
			else:
				print('AQUI E BODYBUILDER!!')


if __name__ == '__main__':
	main()