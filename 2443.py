from  fractions import Fraction
def main():

	entradas = input()
	a,b,c,d = [int(k) for k in entradas.split()]
	soma = Fraction(a,b)+Fraction(c,d)

	lista = str(soma).split('/')

	if len(lista) == 1:
		m = int(lista[0])
		n = 1
		print(m,n)

	else:
		m,n = [int(i) for i in lista]
		print(m,n)

if __name__ == '__main__':
	main()