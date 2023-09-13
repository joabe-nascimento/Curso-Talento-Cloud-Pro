# String fornecida
string = "0-tomate, 1-batata, 2-cenoura, 3-tomate, 4-batata, 5-cenoura"

# Divida a string em uma lista usando ", " como delimitador
itens = string.split(", ")

# Inicialize uma variável para contar os tomates
contagem_tomates = 0

# Inverta a ordem da lista de itens para regar de trás para frente
itens.reverse()

# Percorra a lista de itens invertida e conte os tomates
for item in itens:
    # Verifique se o item contém a palavra "tomate"
    if "tomate" in item:
        contagem_tomates += 1

# Imprima a mensagem inicial
print("O robp regara as plantas de tras para frente, comecando pelo numero 5 e indo ate o numero 0.")

# Verifique se há tomates e imprima a quantidade
if contagem_tomates > 0:
    print(f"Quantidade de tomates que precisam ser regados: {contagem_tomates}")
else:
    print("Não há tomates para regar.")
