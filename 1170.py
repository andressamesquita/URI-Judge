def main():
	n = int(input())
	
	for i in range(1,n+1):
		kilos = float(input())
		dias = 0

		while kilos > 1:
			kilos = (kilos/2)
			dias += 1
			
		print('%i dias'%dias)

if __name__ == '__main__':
	main()