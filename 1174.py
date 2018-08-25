def main():
	vetor = []
	for i in range(100):
		item = int(input())
		vetor.append(item)

	A = []
	for x in vetor:
		if x <= 10:
			A.append(x)
	c = 0
	for x in A:
		print ('A[%i] = %i'%(c,x))
		c += 1

if __name__ == '__main__':
	main()