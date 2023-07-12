# Aula 1 - Funções em Python- Parte 1

# Função com vários argumentos nomeados
def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

# Python não conseguiu identificar qual argumento é qual quando trocamos a ordem
salvar_carro("Fiat", "Palio", 1999, "ABC-1234")

# Mas informando o nome do argumento, o Python consegue identificar mesmo trocando a ordem
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")

# ** significa que todos os argumentos nomeados serão armazenados em um dicionário
# * args significa que todos os argumentos posicionais serão armazenados em uma tupla
# ** kwargs significa que todos os argumentos nomeados serão armazenados em um dicionário
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
