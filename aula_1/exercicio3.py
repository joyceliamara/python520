idade = input('Digite sua idade: ')

caracteres_validos = '0123456789'


for letra in idade:
	if letra not in caracteres_validos:
		print("Você digitou letras inves de números")
		exit()

