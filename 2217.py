def main():

	n = int(input())
	
	for i in range(n):
		pot = int(input())
		if pot % 2 == 0:
			print ('1')
		else:
			print ('9')
		
if __name__ == '__main__':
	main()