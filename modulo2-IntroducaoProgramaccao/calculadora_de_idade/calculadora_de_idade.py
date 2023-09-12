import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (1922-2021): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano de nascimento fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Valor inválido. Por favor, digite um número válido.")

nome_completo = input("Digite seu nome completo: ")
ano_nascimento = obter_ano_nascimento()

idade = calcular_idade(ano_nascimento)

print(f"Nome: {nome_completo}")
print(f"Idade em 2023: {idade} anos")
