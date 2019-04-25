import banco

tolerancia = 15
acertos = 0



while acertos < 3:
	
	for usuario in banco.lista_de_usuarios:
		idade = usuario['idade']

		numero = int(input('Tente adivinhar a idade: '))
		if numero in range(idade - tolerancia, idade + tolerancia):
			acertos = acertos + 1
			print('Voce já acertou: ' + str(acertos))
			if acertos == 3:
				break
print('Fim do Jogo')		

       


