def main():

	dados = [29,10,14,37,13]
	print('Antes: ',dados)

	bubble_sort(dados)
	print('\nDepois: ',dados)

def bubble_sort(dados):

	trocou = True
	contador = 1
	while trocou:
		trocou = False
		for i in range(len(dados) - contador):
			print('*',end='')
			if dados[i] > dados[i+1]:
				aux = dados[i]
				dados[i] = dados[i+1]
				dados[i+1] = aux
				trocou = True
		print ("Contador:",contador)
		contador += 1



if __name__ == '__main__':
	main()