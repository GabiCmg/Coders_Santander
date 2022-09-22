arquivo = open('Aplicacoes/arquivos/dom_casmurro_cap_1.txt','r', encoding='utf-8')
texto = arquivo.read()
print(texto)
arquivo.close()

arquivo = open('Aplicacoes/arquivos/dom_casmurro_cap_1.txt','r', encoding='utf-8')
linha = arquivo.readline()
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()


arquivo = open('Aplicacoes/arquivos/dom_casmurro_cap_1.txt','r', encoding='utf-8')
for linha in arquivo:
    print(linha, end='')
arquivo.close()

with open('Aplicacoes/arquivos/dom_casmurro_cap_1.txt','r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)