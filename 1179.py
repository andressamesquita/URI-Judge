def main():

	par = []
	impar = []
	for i in range(15):
		item = int(input())
		if item % 2 == 0:
			par.append(item)
			if len(par) == 5:
				for i in range(len(par)):
					print ('par[%i] = %i' %(i,par[i]))
				par = []

		else:
			impar.append(item)
			if len(impar) == 5:
				for i in range(len(impar)):
					print ('impar[%i] = %i' %(i,impar[i]))
				impar = []

	if len(impar) > 0:
		for a in range(len(impar)):
			print ('impar[%i] = %i' %(a,impar[a]))

	if len(par) > 0:
		for b in range(len(par)):
			print ('par[%i] = %i' %(b,par[b]))

if __name__ == '__main__':
	main()