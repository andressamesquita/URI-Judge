def main():
	t = input()

	qtd = 0
	for i in t:
		qtd += 1

	if qtd <= 140:
		print ('TWEET')
	else:
		print ('MUTE')

if __name__ == '__main__':
	main()