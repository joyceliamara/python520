idade = input('Digite sua idade: ')

caracteres_validos = '0123456789'
string_vazia = ''

for letra in idade:
	if letra in caracteres_validos:
		string_vazia += letra


print(string_vazia)