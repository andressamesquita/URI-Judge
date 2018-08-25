def main():
	n = int(input())
	c = 1
	while 1:
		sucessor = n + c
		if sucessor % 2 != 0:
			c += 1
		else:
			print(sucessor)
			break

if __name__ == '__main__':
	main()