nomes_paises = ["Brasil", "Argentina", "China", "Canadá", "Japão"]
print("Tamanho da lista: ", len(nomes_paises))

print(nomes_paises[4])

# A contagem de elementos é feita no sentido oposto
print(nomes_paises[-1])

# Altera um elemento da lista 
nomes_paises[3] = "Colômbia"
print(nomes_paises[3])

# Lista elementos de 1 a 2
print(nomes_paises[1:3])

# Lista elementos de 1 a -2
print(nomes_paises[1:-1])

# Lista elementos a partir de 2
print(nomes_paises[2:])

# Lista elementos até 2
print(nomes_paises[:3])

# Lista todos os elementos
print(nomes_paises[:])

# Lista elementos de 2 em 2
print(nomes_paises[::2])

# Inverte a lista
print(nomes_paises[::-1])

# O Brasil está na lista. Resultado booleano TRUE
print("Brasil" in nomes_paises)

# O Brasil NÃO está na lista. Resultado booleano FALSE
print("Canadá" not in nomes_paises)