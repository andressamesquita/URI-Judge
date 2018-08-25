#-*- coding: utf-8 -*-
def main():
	N = int(input())
	minut = int(N / 60)
	hr = int(minut / 60)
	seg = N % 60
	if minut < 60:
		print("%i:%i:%i" %(hr, minut, seg))
	if minut > 60:
		minut_2 = None
		while minut > 60:
			minut_2 = (minut / 60)
			print("%i:%i:%i" %(hr, minut_2, seg))
			if  minut_2 <= 60:
				break
if __name__ == '__main__':
	main()


	"""556 segundos
	quantos minutos existem em 556 segundos?
		556/60 = ?
		(OBS: o resto continua nos segundos)
	quantas hrs existem em "? minutos"?
		? / 60 = "tantas hrs"
	quantos segundos sobram?
		? % 60 = "tantos seg"

		"tantas hrs": "? minutos":"tantos seg"
	***os minutos devem ser de 0 a 60, se maior q isso,
	deve-se dividir novamente até que seja < 60. 
		



		"""