cumprimento = "Olá, "
nome = "Gabriela"
idade = 43
n_filhos = 4

print(cumprimento + nome)

print(nome * 5)

# PRIMEIRO MÉTODO
# print(nome + " tem " + str(idade) + " anos e " + str(n_filhos) + " filhos.")

# SEGUNDO MÉTODO
# print("{} tem {} anos e {} filhos.".format(nome, idade, n_filhos))

# RESUMO
print(f"{nome} tem {idade} anos e {n_filhos} filhos.")

preco_gasolina = 3.476

print("O preço da gasolina hoje está em R$ {:.2f}".format(preco_gasolina))
