# ------------------------------
# LISTA
print('\nLISTA\n')

nomes_cidades = ['São Paulo', 'Londres', 'Tóquio', 'Paris']
for nome in nomes_cidades:
    print(nome)

# Nomes é uma cópia, logo Espirito Santo fez referência logo, não modificou os valores na lista
for nome in nomes_cidades:
    nome = 'Espirito Santo'
print('\n' + str(nomes_cidades))

# Para uma alteração funcional usamos a função range
# FUNÇÃO RANGE
print('\nI. Função Range\n')

print('Veja o incremento do valor posição:\n...')
for posicao in range(len(nomes_cidades)):
    print(posicao)

print('\nAlteramos todos os dados para \'Espírito Santo\', veja a seguir:\n...')
for posicao in range(len(nomes_cidades)):
    nomes_cidades[posicao] = 'Espirito Santo'
print(nomes_cidades)

print('\nOutros exemplos do uso de range:\n...')
print(list(range(10))) # Determina o valor final menos um
print(list(range(2, 10))) # Determina o valor inicial e o final -1
print(list(range(2, 10, 2))) # Determina o valor inicial, valor final - 1 e um incremento de 2, ou seja, a lista contem valores de dois em dois [2, 4, 6, 8]

# ------------------------------
# TUPLA
print('\nTUPLA\n')

nomes_cidades = 'São Paulo', 'Londres', 'Tóquio', 'Paris'
for nome in nomes_cidades:
    print(nome)

# ------------------------------
# DICIONÁRIO
print('\nDICIONÁRIO\n')

cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'populacao_milhoes': 12.2,
}

for chave in cidade:
    print(f'{chave}: {cidade[chave]}')