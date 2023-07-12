# Aula 1 - Funções em Python- Parte 1

# Função é um bloco de código que pode ser executado várias vezes
# Função sem argumento
def exibir_mensagem():
    print("Olá mundo!")

# Função com argumento
def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

# Função com argumento opcional, caso não seja passado nenhum argumento, o valor padrão será "Anônimo"
def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
