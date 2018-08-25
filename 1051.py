def main():
	
	salario = float(input())

	if salario <= 2000:
		print ('Isento')
	
	elif salario >= 2000.01 and salario <= 3000:
		imposto = (salario - 2000)* 0.08
		print ('R$ %.2f'%imposto)
	
	elif salario >= 3000.01 and salario <= 4500.00:
		s = salario - 2000
		imposto = (1000 * 0.08)+((s-1000)*0.18)
		print ('R$ %.2f'%imposto)
	
	elif salario > 4500:
		s = 1000
		ss = 1500
		sal = salario - 4500
		imposto = (s * 0.08) + (ss * 0.18) + (sal * 0.28)
		print ('R$ %.2f'%imposto)

if __name__ == '__main__':
	main()