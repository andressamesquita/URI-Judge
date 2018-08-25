def main():
	n = int(input())

	if n == 1:
		print ('Top 1')
	elif n > 1 and n <= 3:
		print ('Top 3')
	elif n > 3 and n <= 5:
		print ('Top 5')
	elif n > 5 and n <= 10:
		print ('Top 10')
	elif n > 10 and n <= 25:
		print ('Top 25')
	elif n > 25 and n <= 50:
		print ('Top 50')
	elif n > 50 and n <= 100:
		print ('Top 100') 

if __name__ == '__main__':
	main()