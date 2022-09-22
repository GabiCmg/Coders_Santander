from urllib import request
import requests

url = 'https://open.er-api.com/v6/latest'

req = requests.get(url)

# Verificar se a url está funcional
print(req.status_code)

# Esse método pega o json retornado pela api e transforma em um dicionário
dados = req.json()

print(dados)

valor_reais = float(input('Informe o valor em reais a ser convertido: \n'))
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dólar valor US${(valor_reais / cotacao):.2f}')