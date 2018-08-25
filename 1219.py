def main():

	entradas = input()
	a,b,c = [int(k) for k in entradas.split()]

	a_circ_grande = 3.14 * ((a/2)**2)
	a_tri = (b*c)/2

	sun = sunflowers(a_circ_grande,a_tri)

def sunflowers(a_circ_grande,a_tri):

	area_sun = a_circ_grande - a_tri
	return area_sun





if __name__ == '__main__':
	main()