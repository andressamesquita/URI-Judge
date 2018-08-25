def main():

	n = int(input())
	c = 0
	for i in range(n):
		tipo = input()
		entradas = input()
		r,g,b = [int(k) for k in entradas.split()]
		c += 1
		
		if tipo == 'eye':
			p = (0.30 * r) + (0.59 * g) + (0.11 * b)
		elif tipo == 'mean':
			p = (r+g+b)/3
		elif tipo == 'max':
			p = max([r,g,b])
		elif tipo == 'min':
			p = min([r,g,b])
		
		print('Caso #%i: %i' %(c,int(p)))

if __name__ == '__main__':
	main()