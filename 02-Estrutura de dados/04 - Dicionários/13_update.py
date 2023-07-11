# Aula 02 - Métodos da classe dict

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Método update(), atualiza o dicionário com os pares de chave-valor informados
contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)
