# Aula 01 - Dicionários: Criação e acesso aos dados

# Criando um dicionário usando chaves
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

# Criando um dicionário usando a função dict()
pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

# Adicionando uma nova chave ao dicionário
# {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
pessoa["telefone"] = "3333-1234"
print(pessoa)
