def main():

	entradas = input()
	a,b = [int(i) for i in entradas.split()]

	k = b-a

	c = 1
	p = k
	while p < b:
		p += k
		c += 1
		if p > b:
			break

	print(c)



if __name__ == '__main__':
	main()