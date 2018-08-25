def main():
	decimal = int(input())
	hexadecimal = []
	valor = ''
	while decimal != 0:
		valor = str(decimal % 16)
		decimal = decimal // 16

		if valor == '10':
			valor = 'A'


		elif valor == '11':
			valor = 'B'
	
		elif valor == '12':
			valor = 'C'
	
		elif valor == '13':
			valor = 'D'
	
		elif valor == '14':
			valor = 'E'
	
		elif valor == '15':
			valor = 'F'

		hexadecimal.append(valor)

	print ("".join(hexadecimal)[::-1])

if __name__ == '__main__':
	main()