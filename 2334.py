def main():

	while True:
		n = int(input())
		if n == -1:
			break
		elif n == 0:
			new_n = 0
			print ('%i'%new_n)
		else:
			new_n = n-1
			print('%i'%new_n)

if __name__ == '__main__':
	main()