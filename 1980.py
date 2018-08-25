from math import gamma
def main():

	fat = 1
	while True:
		s = input()
		
		if s == '0':
			break
		else:
			tamanho = len(s)
			f = fatorial(tamanho)
			print(int(f))

def fatorial(a):

	if int(a) == 0 or int(a) == 1:
		return 1
							
	else:
		cont = int(a)-1
		fat = int(a)
		while cont > 1:
			if int(a) != 0 and int(a) != 1:
				fat *= cont
				cont -= 1

		return fat


if __name__ == '__main__':
	main()