# String fornecida
string = "0-tomate, 1-tomate, 2-tomate, 3-batata, 4-batata, 5-batata"

# Divida a string em uma lista usando ", " como delimitador
itens = string.split(", ")

# Inicialize uma variável para contar as batatas
contagem_batatas = 0

# Percorra a lista de itens e conte as batatas
for item in itens:
    # Verifique se o item contém a palavra "batata"
    if "batata" in item:
        contagem_batatas += 1

# Imprima o resultado
print(f"Quantidade de batatas que precisam ser regadas: {contagem_batatas}")
