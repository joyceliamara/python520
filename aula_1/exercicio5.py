




def receber_idade():
	idade = input('Digite a sua idade: ')
	idade =  int(idade)
	if idade <= 0:
		raise Exception('idade menor do que zero')
	return idade

def imprimir_idade(idade):
	print('Você disse que tem {} anos.'.format(idade))

#fluxo feliz
try:
	
	idade = receber_idade()
	imprimir_idade(idade)

except ValueError:
	print("Voce digitou um caracter invalido")
except Exception as err:
	print(err)


exit()

idade = input("Digite a sua idade: ")

#aqui entra a validação de caracter não numerico
for letra in idade:
	if letra not in '0123456789':
		print('caracter invalido')
		exit()

#aqui entra a validação se numero negativo
if int(idade) < 0:
	print('numero negativo')
	exit()

#aqui entra a validacao de numero muito
if int(idade) > 100:
	print('Vocẽ pode não existir')
	exit()

idade = int()