BANCO_DE_DADOS = []
BANCO_DE_DADOS.append({
	'email' : 'joyce.marinheiro@linux.com',
	'idade' : '28',
	'senha' : 'admin'
})


class InvalidEmailError(Exception):
	pass

class InvalidAgeError(Exception):
	pass

class UsuarioCadastradoError(Exception):
	pass

class SenhaInvalidaError(Exception):
	pass


def receber_novo_usuario():

	email = input('Digite seu email: ')

	if '@' not in email:
		raise InvalidEmailError

	idade =  int(input('Digite sua idade: '))

	if idade <= 0:
		raise InvalidAgeError

    # retorna o usuario criado 
	return{
		'email': email,
		'idade': idade, 
		'senha': input('Digite sua senha: ')
	}



def cadastrar_usuario(usuario):
	#verificar se o usuario já existe no banco
	for usuario_cadastrado in BANCO_DE_DADOS:
		if usuario_cadastrado['email'] == usuario['email']:
			raise UsuarioCadastradoError
	BANCO_DE_DADOS.append(usuario)

def verificar_senha(usuario):
	senha = input('Digite sua senha: ')
	if usuario['senha'] != senha:
		raise SenhaInvalidaError

try:
	usuario = receber_novo_usuario()
	cadastrar_usuario(usuario)
	verificar_senha(usuario)

	print('Usuario cadastrado com sucesso')

except InvalidEmailError as err:
	print('Email invalido')

except InvalidAgeError as err:
	print('Idade invalida')

except UsuarioCadastradoError as err:
	print('Usuario já cadastrado')
	
except ValueError as err:
	print('Erro da linguagem Python')

except SenhaInvalidaError:
	print('Senha Inválida')



