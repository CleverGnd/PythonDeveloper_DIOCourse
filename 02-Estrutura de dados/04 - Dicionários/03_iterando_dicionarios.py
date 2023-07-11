# Aula 01 - Dicionários: Criação e acesso aos dados

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

# Iterando sobre um dicionário usando o for
for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

# Iterando sobre um dicionário usando o for e o método items()
for chave, valor in contatos.items():
    print(chave, valor)
