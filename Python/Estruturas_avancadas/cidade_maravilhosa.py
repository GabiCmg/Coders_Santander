nome_cidade = input("Que cidade do Brasil é conhecida como \"Cidade Maravilhosa\" ? ")
nome_cidade = nome_cidade.strip()
while nome_cidade.lower() != "rio de janeiro":
    print('Tente novamente.')
    nome_cidade = input("Que cidade do Brasil é conhecida como \"Cidade Maravilhosa\" ? ")
print("Muito bem! Você realmente conhece o Brasil.")