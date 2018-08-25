def main():

	while True:
		try:
			entrada = int(input())
			senha = entrada - 1
			print ('%i'%senha)

		except:
			break

if __name__ == '__main__':
	main()