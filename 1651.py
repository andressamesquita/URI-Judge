def main():

	entrada = input()
	w,h = [int(i) for i in entrada.split()]

	v = ((w/2)**2) * (h/2)

	print ('%.3f' %v)

if __name__ == '__main__':
	main()