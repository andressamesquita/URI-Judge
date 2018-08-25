import sys
def main():
	
	soma_nota = 0
	qtd = 0
	
	while True:
		X = float(input())
		
		if X < 0 or X > 10:
			print ('nota invalida')
		elif 0 <= X <= 10:
			qtd += 1
			soma_nota += X
	
		if qtd == 2:
			media = soma_nota / 2
			print ('media = %.2f' %media)
				
			opcao()

def opcao():

	opcao = 0
	while opcao != 1:
		print ('novo calculo (1-sim 2-nao)')
		opcao = int(input())
		
		if opcao == 2:
			sys.exit(0)
		elif opcao == 1:
			return main()


if __name__ == '__main__':
	main()