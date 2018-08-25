#-*-coding: utf-8 -*-
def main():
	X = int(input())
	impar = 0
	if X % 2 != 0:
		impar1 = X
		print ("%i" %impar1)
	else:
		impar1 = X + 1
		print ("%i" %impar1)

	impar2 = impar1 + 1
	if  impar2 % 2 != 0:
		print ("%i" %impar2)
	else:
		impar2 = impar1 + 2
		print ("%i" %impar2)
	
	impar3 = impar2 + 1
	if impar3 % 2 != 0:
		print ("%i" %impar3)
	else:
		impar3 = impar2 + 2
		print ("%i" %impar3)
	
	impar4 = impar3 + 1	
	if impar4 % 2 != 0:
		print ("%i" %impar4)
	else:
		impar4 = impar3 + 2
		print ("%i" %impar4)
	
	impar5 = impar4 + 1	
	if impar5 % 2 != 0:
		print ("%i" %impar5)
	else:
		impar5 = impar4 + 2
		print ("%i" %impar5)
	
	impar6 = impar5 + 1	
	if impar6 % 2 != 0:
		print ("%i" %impar6)
	else:
		impar6 = impar5 + 2
		print ("%i" %impar6)
if __name__ == '__main__':
	main()