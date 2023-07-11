# Aula 02 - Métodos da classe dict

contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# Método copy(), retorna uma cópia do dicionário
copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

# {"nome": "Guilherme", "telefone": "3333-2221"}
print(contatos["guilherme@gmail.com"])

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}
