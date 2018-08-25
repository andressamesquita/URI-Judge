def main():

	while True:
		try:
		
			entradas = input().split()
			v = int(entradas[0])
			t = int(entradas[1])

			resultado = v * (2 * t)
			print (resultado)
		
		except:
			break



if __name__ == '__main__':
	main()