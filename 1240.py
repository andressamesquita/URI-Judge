def main():
	n = int(input())

	for i in range(n):
		entradas = input().split()
		A,B = entradas

		if len(B) > len(A):
			print ('nao encaixa')

		else:

			inverso_B = B[::-1]
			inverso_A = A[::-1]

			ok = 0
			
			for u in range(len(inverso_B)):
				
				if inverso_A[u] != inverso_B[u]:
					ok = 1
					break

			if ok == 1:
				print ('nao encaixa')
			else:
				print ('encaixa')
										

if __name__ == '__main__':
	main()