# Aula 01 - Dicionários: Criação e acesso aos dados

dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

# Acessando os dados do dicionário pela chave
print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

# Alterando o valor de uma chave
dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}
