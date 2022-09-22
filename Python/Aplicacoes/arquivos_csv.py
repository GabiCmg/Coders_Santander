import csv

with open('Aplicacoes/arquivos/brasil_covid.csv','r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)

with open('Aplicacoes/arquivos/brasil_covid.csv','r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    # A função next() pula uma das iterações
    header = next(leitor)
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)

# ------------------------------
# O mesmo código sem fazer o uso da biblioteca

with open('Aplicacoes/arquivos/brasil_covid.csv','r', encoding='utf-8') as csv_file:
    linhas = csv_file.read() # Ler as linhas
    linhas = linhas.split('\n') # Separar em lista
    for linha in linhas:
        linha = linha.split(',') # Separa o valor dos dados
        print(linha)