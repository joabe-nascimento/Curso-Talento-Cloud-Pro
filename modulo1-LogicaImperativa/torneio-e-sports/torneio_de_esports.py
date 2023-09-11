# Solicitar o nome da equipe ao usuário
nome_equipe = input("Digite o nome da equipe: ")

# Loop para gerar etiquetas para os 5 membros da equipe
for i in range(1, 6):
    etiqueta = f"{nome_equipe} - {i}"
    print(etiqueta)
