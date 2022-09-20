# EXEMPLO I

# Passo I: Definir essa função
def hello():
    print('Hello, world!')
# Passo II: Camar essa função
hello()

# ------------------------------
# EXEMPLO II
def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcula_media(10, 10, 10)
print(resultado)

resultado2 = calcula_media(valor1 = 9, valor2 = 10, valor3 = 9)

# EXEMPLO III

print('Olá,', end = ' ')
print('mundo!')

def calcula_media(valor1 = 0, valor2 = 0, valor3 = 0):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcula_media()
print(resultado)