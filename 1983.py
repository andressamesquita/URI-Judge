def main():
	n = int(input())

	notas = []
	matriculas = []
	for i in range(n):
		entradas = input()
		matricula,nota = int(entradas.split()[0]),float(entradas.split()[1])

		if nota >= 8.0:
			notas.append(nota)
			matriculas.append(matricula)
			maxima = sum()







if __name__ == '__main__':
	main()