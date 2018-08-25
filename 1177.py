def main():
	n = int(input())

	c = 0
	a = 0
	while c < 1000:
		print ('N[%i] = %i' %(c,a))
		a += 1
		c += 1
		if a == n:
			a = 0

if __name__ == '__main__':
	main()