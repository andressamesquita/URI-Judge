def main():
	x = int(input())

	for i in range(1,x+1):
		t = input()

		seg = 0
		for n in t:
			seg += 0.01

		print ('%.2f'%seg)

if __name__ == '__main__':
	main()