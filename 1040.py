#-*- coding: utf-8 -*-
def main():
	entrada = input()
	valores = entrada.split(" ")
	notas = [float(nota) for nota in valores]
	N1, N2, N3, N4 = notas
	media = (N1*2 + N2*3 + N3*4 + N4*1)/(2+3+4+1)
	if media >= 7.0:
		print ("Media: %.1f" %media)
		print ("Aluno aprovado.")
	elif media < 5.0:
		print ("Media: %.1f" %media)
		print ("Aluno reprovado.")
	elif 5.0 <= media <= 6.9:
		print ("Media: %.1f" %media)
		print ("Aluno em exame.")
		exame = float(input())
		MEDIA_final = (exame + media)/2
		if MEDIA_final >= 5.0:
			print ("Nota do exame: %.1f" %exame)
			print ("Aluno aprovado.")
			print ("Media final: %.1f" %MEDIA_final)
		elif MEDIA_final <= 4.9:
			print ("Nota do exame: %.1f" %exame)		
			print ("Aluno reprovado.")
			print ("Media final: %.1f" %MEDIA_final)

if __name__ == '__main__':
	main()