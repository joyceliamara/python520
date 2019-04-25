import banco

#print(banco.lista_de_usuarios)

#exercicio1:
#imprima somente os usuarios
#cujos emails contenham as letras:
#'a' ou 'k' ou 'm' ou 'l'
#e cujas idades sejam
# maior que 30 e menor que 40

#dica do exercicio

# Condições OU
#primeira parte
for usuario in banco.lista_de_usuarios:

	email = usuario['email'].lower()
	idade = usuario['idade']

	condicao_1 = 'a' in email
	condicao_1 = condicao_1 or 'k' in email
	condicao_1 = condicao_1 or 'm' in email
	condicao_1 = condicao_1 or 'l' in email 

	condicao_2 = idade > 30 and idade < 40
	
	
	if condicao_1 and condicao_2:
		print(usuario)

#solucao2:
for usuario in banco.lista_de_usuarios:
	email = usuario['email'].lower()
	idade = usuario['idade']

	condicao_1 = False
	letras = ['a','k','m','k']
	for letra in letras:
		condicao_1 = condicao_1 or letra in email

	condicao_2 = idade > 30 and idade < 40

	if condicao_1 and condicao_2:
		print(usuario)
#fim		




if 2 < 4 or 5 < 10:
		print('Condição OU')

#condição E
if 2 < 4 and 5 < 10:
	print('Condição AND')

#testar se uma letra está em uma string
if 'c' in 'LuCas'.lower():
	print('Lucas tem C')

#Obs: A função lower() converte uma string
# para letra minuscula
print('LUCAS'.lower()) #imprime 'lucas' tudo minusculo

condicao_1 ='c' in 'lucas'
condicao_2 = 20 < 40

if condicao_1 and condicao_2:
	print('opaa')
