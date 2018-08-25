def main():

	while True:
		try:

			entradas = input()
			first_soma = multiplicando(entradas)
			second_soma = multip(entradas)
			b1 = confe_b1(first_soma)
			b2 = confer_b2(second_soma)

			cpf = entradas[:3]+'.'+entradas[3:6]+'.'+entradas[6:9]+'-'+str(b1)+str(b2)
			print(cpf)

		except:
			break

def multiplicando(entradas):

	soma = 0
	c = 1
	for i in entradas:
		soma += int(i)*c
		c += 1
		if c == 10:
			break
	return soma

def multip(entradas):

	
	soma = 0
	c = 9
	for i in entradas:
		soma += int(i)*c
		c -= 1
		if c == 0:
			break
	return soma

def confe_b1(first_soma):

	b1 = first_soma % 11

	if first_soma % 11 == 10:
		b1 = 0

	return b1

def confer_b2(second_soma):

	b2 = second_soma % 11

	if second_soma  % 11 == 10:
		b2 = 0
	
	return b2



if __name__ == '__main__':
	main()