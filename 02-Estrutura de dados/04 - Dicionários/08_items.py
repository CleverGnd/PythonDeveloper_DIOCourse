# Aula 02 - Métodos da classe dict

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Método items(), retorna uma lista de tuplas, cada tupla contém um par de chave-valor
# dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
resultado = contatos.items()
print(resultado)
