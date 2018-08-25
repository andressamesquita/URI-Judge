def main():

	entradas =''
	n1 = ''
	n2 = ''
	carry = 0
	qtd = 0

	while True:
		entradas = input().split()
		n1 = entradas[0]
		n2 = entradas[1]

		if n1 == n2 == '0':
			break
		
		n1 = int(n1[::-1])
		n2 = int(n2[::-1])

		u_n1 = 


		'''
		for letra in n1[::-1]:
			for l in n2[::-1]:
				if int(letra) + int(l) >= 10:
					carry += 1
		
		if carry == 0:
			print ('No carry operation.')
		elif carry == 1:
			print ('%i carry operation.' %carry)
		else:
			print ('%i carry operations.'%carry)

		carry = 0
'''
		
if __name__ == '__main__':
	main()