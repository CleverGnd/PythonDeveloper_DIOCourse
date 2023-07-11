# Aula 02 - Métodos da classe dict

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Método pop(), remove a chave e retorna o valor da chave informada
# {'nome': 'Guilherme', 'telefone': '3333-2221'}
resultado = contatos.pop("guilherme@gmail.com")
print(resultado)

# Caso a chave não exista, retorna o valor padrão {}
resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)
