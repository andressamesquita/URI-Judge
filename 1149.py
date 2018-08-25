def main():

	valores = input().split()
	A = int(valores[0])
	tamanho = len(valores)

	for i in range(1,tamanho+1):
		n = int(valores[i])
		if n > 0:
			break
	
	soma = 0
	contador = 0
	while contador < n:
		soma += A
		A += 1
		contador += 1

	print (soma)

if __name__ == '__main__':
	main()