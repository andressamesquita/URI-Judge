def main():
	
	n = int(input())
	a,b = 0,1
	c = 0
	fib = [a,b]
	for i in range(1,n):
		c = a
		a = b
		b = a + c
		fib.append(a)

	print(fib)

if __name__ == '__main__':
	main()