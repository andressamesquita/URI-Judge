def main():
	X = int(input())
	Z = int(input())

	while Z <= X:
		Z = int(input())
		if Z > X:
			exceded_Z(X,Z)

def exceded_Z(X,Z):
	
	qtd = 0
	soma = 0
	while soma < Z:
		soma += X
		X += 1 

		qtd += 1
	
	print ('%i'%qtd)


if __name__ == '__main__':
	main()