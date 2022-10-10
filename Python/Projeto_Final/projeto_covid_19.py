import requests as r
import csv
# Essa biblioteca tem três objetos que representam tempo time | date | datetime
import datetime as dt
from PIL import Image
from IPython.display import display
from urllib.parse import quote

#
# 
#  
# PARTE I
# 
# 
# 

url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)

# print(resp.status_code)

raw_data = resp.json()

# print(raw_data[0])

final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

final_data.insert(0, ['Confirmados', 'Óbitos', 'Recuperados', 'Ativos', 'Data'])

# Váriavel em caps simboliza uma constante, ou seja, não há alteração no valor durante o código
CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4

for i in range(1, len(final_data)):
    # Observação e campo relativo a ser manipulado
    final_data[i][DATA] = final_data[i][DATA][:10]

with open('Projeto_Final/arquivos/brasil_covid.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

for i in range(1, len(final_data)):
    # .strptime -> Realiza um parse de string para um tipo data
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')

# 
# 
# 
# PARTE II
# [Api responsável por renderizar gráficos]
# 
# 

def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return[
            {
                'label': labels[0],
                'data': y
            }
        ]

def set_title(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title': title,
        'display': display
    }

def create_chart(x, y, labels, kind='bar', title=''):
    datasets = get_datasets(y, labels)
    options = set_title(title)

    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    return chart

def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    # imagem
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content

def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)

def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)

y_data_1 = []
for obs in final_data[1::10]:
    y_data_1.append(obs[CONFIRMADOS])

y_data_2 = []
for obs in final_data[1::10]:
    y_data_2.append(obs[RECUPERADOS])

labels = ['Confirmados', 'Recuperados']

x = []
for obs in final_data[1::10]:
    # transforma date em string
    x.append(obs[DATA].strftime('%d/%m/%Y'))

chart = create_chart(x, [y_data_1, y_data_2], labels, title='Gráfico confirmados vs recuperados')
chart_content = get_api_chart(chart)
save_image('Projeto_Final/imagens/meu_primeiro_grafico.png', chart_content)
display_image('Projeto_Final/imagens/meu_primeiro_grafico.png')

def get_api_qrcode(link):
    text = quote(link) # parsing do link para url
    url_base = 'https://quickchart.io/qr'
    resp = r.get(f'{url_base}?text={text}')
    return resp.content

url_base = 'https://quickchart.io/chart'
link = f'{url_base}?c={str(chart)}'
save_image('Projeto_Final/imagens/qr_code.png', get_api_qrcode(link))
display_image('Projeto_Final/imagens/qr_code.png')