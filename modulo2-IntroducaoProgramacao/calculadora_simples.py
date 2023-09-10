def calculadora(num1, num2, operacao):
    if operacao == 1:
        resultado = num1 + num2
    elif operacao == 2:
        resultado = num1 - num2
    elif operacao == 3:
        resultado = num1 * num2
    elif operacao == 4:
        if num2 != 0:  # Verifica se não estamos tentando dividir por zero
            resultado = num1 / num2
        else:
            resultado = 0
    else:
        resultado = 0  # Se a operação não for válida, o resultado é 0
    
    return resultado

# Exemplos de uso:
print(calculadora(5, 3, 1))  # Soma: 5 + 3 = 8
print(calculadora(10, 4, 2))  # Subtração: 10 - 4 = 6
print(calculadora(7, 2, 3))  # Multiplicação: 7 * 2 = 14
print(calculadora(8, 0, 4))  # Divisão por zero: resultado = 0
print(calculadora(5, 3, 5))  # Operação inválida: resultado = 0
