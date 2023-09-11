def alocar_area_restaurante():
    print("Bem-vindo ao nosso restaurante! Vamos ajudá-lo a encontrar o melhor lugar para se acomodar.")
    num_pessoas = int(input("Quantas pessoas estão no seu grupo? "))
    fumantes = input("Alguém em seu grupo é fumante? (Sim/Não) ").strip().lower()
    animais_estimacao = input("Algum de vocês trouxe um animal de estimação? (Sim/Não) ").strip().lower()

    if num_pessoas >= 5:
        print("Perfeito! Vamos encontrar um ótimo lugar para o seu grupo no 1º andar.")
    elif fumantes == "sim" or animais_estimacao == "sim":
        print("Entendo, temos uma área externa aconchegante que atenderá às suas necessidades.")
    else:
        print("Sem problemas, o térreo é o local perfeito para vocês aproveitarem a sua refeição.")

if __name__ == "__main__":
    alocar_area_restaurante()
