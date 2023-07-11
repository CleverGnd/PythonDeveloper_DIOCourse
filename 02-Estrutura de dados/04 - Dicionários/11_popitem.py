# Aula 02 - Métodos da classe dict

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Método popitem(), remove a última chave e retorna o valor da chave removida
# ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
resultado = contatos.popitem()
print(resultado)

# contatos.popitem()  # KeyError
