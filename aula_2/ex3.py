
lista_de_usuarios = []

arquivo = open('relatorio.csv', 'r')
for linha in arquivo.readlines():
	registro = linha.split(';')
	usuario= {
		'nome'     : registro[0],
		'idade'    :registro[1],
		'email'    :registro[2],
		'sexo'     :registro[3],
		'endereco' :registro[4]
	}
	lista_de_usuarios.append(usuario)
	print(lista_de_usuarios)


exit()

arquivo = open('usuarios.txt', 'r')
for linha in arquivo.readlines():
	print(linha)
arquivo.close()







arquivo = open('usuarios.txt', 'w')
arquivo.write('hello, world')
arquivo.close()

arquivo = open('usuarios.txt', 'a')
for i in range(100):
	arquivo.write(str(i) + '\n')
	print(str(i))
arquivo.close()

arquivo = open('usuarios.txt', 'r')
for i in arquivo.readlines():
	print(str(i))
arquivo.close()