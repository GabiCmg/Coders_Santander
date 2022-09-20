# DICIONÁRIO
dados_cidade = {
    'nome': 'São Paulo',
    'estado': 'São Paulo',
    'area_km2': 1521,
    'populacao_milhoes': 12.10,
}

# ------------------------------
# TIPO DE DADO
print('\n TIPO DE DADO \n')

print(type(dados_cidade))

# ------------------------------
# ADICIONA E ALTERA VALORES
print('\n ADICIONA E ALTERA VALORES \n')

dados_cidade['pais'] = 'Brasil'
dados_cidade['estado'] = '1500'
print(dados_cidade['nome'])
print(dados_cidade['estado'])

# ------------------------------
# MÉTODO COPY
print('\n MÉTODO COPY \n')

# Duplica valores, mas ambos serão alterdos no fim - o arquivo original e a cópia
# dados_cidade_2 = dados_cidade
# dados_cidade_2['nome'] = 'Santos'
# print(dados_cidade_2)

# Realiza uma cópia e modifica um elemento nesta cópia
dados_cidade_3 = dados_cidade.copy()
dados_cidade_3['nome'] = 'Rio de Janeiro'
print(dados_cidade_3)

# ------------------------------
# UPDATE DE VALORES
print('\n UPDATE DE VALORES \n')

novos_dados = {
    'populacao_milhoes': 15,
    'fundacao': '25/01/1554'
}

dados_cidade.update(novos_dados)
print(dados_cidade)

# ------------------------------
# MÉTODO GET
print('\n MÉTODO GET \n')

print(dados_cidade.get('prefeito'))

# ------------------------------
# DICIONÁRIO EM LISTA
print('\n DICIONÁRIO EM LISTA \n')

print(dados_cidade.keys())
print('-----')
print(dados_cidade.values())
print('-----')
print(dados_cidade.items())