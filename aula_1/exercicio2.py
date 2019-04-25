#Exercicio2
# Dada uma lista de numeros
#escrever um algoritmo que calcula
# a media dos numeros nesta lista
#salvar em uma variavel e imprimir


lista_de_numeros = [1,2,3,4,5,6]

soma = 0
tamanho = 0

for numero in lista_de_numeros:
	soma = soma + numero
	tamanho = tamanho + 1

print(soma / tamanho)








