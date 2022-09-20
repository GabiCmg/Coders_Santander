def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media

resultado = calcula_media(10, 10, 10)
print(resultado)

# Exemplo que mostra os valores que args recebe, neste caso recebe uma tupla com três valores
def calcula_media(*args):
    print(args, type(args))

calcula_media(10, 8, 9)

# Args recebe n valores, não há limite
def calcula_media(*args):
    soma = sum(args)
    media = soma / len(args)
    return media

print(calcula_media(10, 8, 9))

# O valor deve ser explicito para o parâmetro de margem caso contrário os valores continuam a ser inseridos em *args automaticamente
def calcula_media(*args, margem):
    soma = sum(args)
    media = soma / len(args)
    return media + margem

print(calcula_media(10, 8, 9, margem = 0.3))

# Kwargs (Key word arguments) -> Uma técnica de visualização de dados. As funções dessa biblioteca, recebe uma série de parâmetros que são padrão, principalmente no caso de visualização de gráficos, à diferentes funções para diferentes gráficos, no entanto, performam da mesma maneira.
def print_info(**kwargs):
    print(kwargs, type(kwargs))

# Ao utilizar essa técnica todos os parametros que serão dedicados ao kwargs devem ser nomeados
# Chave = nome da variavel e valor = valor
print_info(nome = 'Gabriela', sobrenome = 'Camargo')