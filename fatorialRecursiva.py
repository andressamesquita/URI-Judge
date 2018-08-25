def main():
	n = int(input())
	print ('%i' %fatorial(n))

def fatorial(n):
	
	if n == 1:
		return 1
	else:
		return n * fatorial(n-1)
		
if __name__ == '__main__':
	main()