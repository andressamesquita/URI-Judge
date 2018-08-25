def main():
	entradas = input().split()
	altura,canos = int(entradas[0]),int(entradas[1])

	entradas = input()
	valores = entradas.split()
	lista = [int(n) for n in valores]

	
	c = 1
	a = 0
	while canos != 0:
		if subt <= altura:
			c += 1
			canos -= 1
			a += 1
			if canos == 0:
				print ('YOU WIN')
		else:
			print ('GAME OVER')
			break
	

if __name__ == '__main__':
	main()