def main():

	entradas = input()
	lista = [float(num) for num in entradas.split()]

	nota_final = sum(lista) - max(lista) - min(lista)

	print('%.1f'%nota_final)

if __name__ == '__main__':
	main()