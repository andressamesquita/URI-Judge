def main():
	texto = input()

	cont = 0
	for i in texto:
		if i == '_':
			cont += 1
			if cont == 1:
				texto.replace('_','<i>')
			elif cont == 2:
				i = '</i>'
		
		elif i == '*':
			cont += 1
			if cont == 1:
				i = '<b>'
			elif cont == 2:
				i = '</b>'
		cont = 0
	print (texto)
	


if __name__ == '__main__':
	main()