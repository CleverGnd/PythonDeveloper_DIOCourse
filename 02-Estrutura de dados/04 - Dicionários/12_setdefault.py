# Aula 02 - Métodos da classe dict

contato = {"nome": "Guilherme", "telefone": "3333-2221"}

# Método setdefault(), retorna o valor da chave informada. Caso a chave não exista, cria a chave com o valor padrão
contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}
