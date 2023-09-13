# String fornecida
string = "0-tomate, 1-tomate, 2-batata, 3-batata, 4-tomate, 5-tomate"

# Divida a string em uma lista usando ", " como delimitador
itens = string.split(", ")

# Inicialize uma variável para contar os tomates
contagem_tomates = 0

# Percorra a lista de itens e conte os tomates
for item in itens:
    # Verifique se o item contém a palavra "tomate"
    if "tomate" in item:
        contagem_tomates += 1

# Imprima o resultado
print(f"Quantidade de tomates que precisam ser regados: {contagem_tomates}")
