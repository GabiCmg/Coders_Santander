import csv

# newline = '' para não haver linhas vazias no csv
with open('Aplicacoes/arquivos/users.csv','w', encoding='utf-8', newline='') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'genero'])
    escritor.writerow(['Gabriela', 'Camargo', 'gabriela.camaroli@gmail.com', 'Feminino'])