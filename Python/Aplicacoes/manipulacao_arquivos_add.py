with open('Aplicacoes/arquivos/dom_casmurro_cap_1.txt','w', encoding='utf-8') as arquivo:
    arquivo.write('Essa é uma linha que eu escrevi usando Python\n')
    arquivo.write('Essa é a segunda linha que eu escrevi usando Python\n')

with open('Aplicacoes/arquivos/dom_casmurro_cap_1.txt','a', encoding='utf-8') as arquivo:
    arquivo.write('Essa é a terceira linha.')

with open('Aplicacoes/arquivos/dom_casmurro_cap_1.txt','r', encoding='utf-8') as arquivo:
    print(arquivo.read(), end='')