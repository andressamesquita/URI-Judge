def main():

	entradas_1 = input()
	entradas_2 = input()

	n1,dist1,vel1 = [int(i) for i in entradas_1.split()]
	n2,dist2,vel2 = [int(k) for k in entradas_2.split()]

		
	if dist1 / vel1 < dist2 / vel2:
		print('%i'%n1)
	else:
		print('%i'%n2)

if __name__ == '__main__':
	main()