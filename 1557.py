def main():
	
	while True:
		
		ordem = int(input())
		
		if ordem == 0:
			break
		else:
			matriz = []
			for i in range(ordem):
				matriz.append([])
				for j in range(1,ordem+1):
					elemento = j
					matriz[i].append(elemento)
					j *= 2

		for i in range(len(matriz)):
			for j in range(len(matriz[i])):
				print (matriz[i][j],end = ' ')
			print ('')





if __name__ == '__main__':
	main()