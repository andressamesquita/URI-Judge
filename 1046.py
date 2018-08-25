#-*- coding: utf-8-*-
def main():
	entrada = input()
	numeros = entrada.split(" ")
	valores = [int(numb) for numb in numeros]
	inicio, fim = valores
	
	hrs = 0
	novo_inicio = 0
	while inicio < fim:
		hrs = hrs + 1
		if inicio != fim:
			inicio = inicio + 1

		elif inicio == fim:
			break
			print("O JOGO DUROU %i HORAS" %hrs)

		elif inicio == 24:
			novo_inicio = novo_inicio + 1
			hrs = hrs + 1
		if novo_inicio == fim:
			break
			print("O JOGO DUROU %i HORAS" %hrs)



if __name__ == '__main__':
	main()