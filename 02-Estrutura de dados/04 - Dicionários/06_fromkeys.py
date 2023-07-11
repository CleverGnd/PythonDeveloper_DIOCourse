# Aula 02 - Métodos da classe dict

# Método fromkeys(), permite a criação de chaves sem valores
# {"nome": None, "telefone": None}
resultado = dict.fromkeys(["nome", "telefone"])
print(resultado)

# Também é possível definir um valor pafrão para as chaves
# {"nome": "vazio", "telefone": "vazio"}
resultado = dict.fromkeys(["nome", "telefone"], "vazio")
print(resultado)
