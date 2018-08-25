def main():
	entradas = input()
	dias_ini = int(entradas.split()[1])

	entradas = input()
	hh_ini = int(entradas.split(':')[0])
	mm_ini = int(entradas.split(':')[1])
	ss_ini = int(entradas.split(':')[2])

	entradas = input()
	dias_fim = int(entradas.split()[1])

	entradas = input()
	hh_finish = int(entradas.split(':')[0])
	mm_finish = int(entradas.split(':')[1])
	ss_finish = int(entradas.split(':')[2])

	
	seg_total_ini = (dias_ini*86400)+(hh_ini*3600)+(mm_ini*60)+(ss_ini)
	seg_total_finish = (dias_fim*86400)+(hh_finish*3600)+(mm_finish*60)+(ss_finish)

	dif = seg_total_finish - seg_total_ini
	

	qtd_dia = dif//86400
	qtd_hh = (dif % 86400) // 3600
	qtd_mm = ((dif % 86400) % 3600) // 60
	qtd_ss = ((dif % 86400) % 3600) % 60

	print ('%i dia(s)'%qtd_dia)
	print ('%i hora(s)'%qtd_hh)
	print ('%i minuto(s)'%qtd_mm)
	print ('%i segundo(s)'%qtd_ss)

if __name__ == '__main__':
	main()