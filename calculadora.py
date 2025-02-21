# Funções para operações matemáticas básicas
def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def multiplicacao(a, b):
    return a * b


def divisao(a, b):
    # Evitar divisão por zero
    if b == 0:
        return "Divisão por zero não permitida!"
    return a / b


# Programa principal
def calculadora():
    # Solicitar o número de repetições
    repeticoes = int(input("Digite o número de repetições: "))

    for i in range(repeticoes):
        # Ler os valores de A e B
        a = float(input(f"Interação {i + 1} - Digite o valor de A: "))
        b = float(input(f"Interação {i + 1} - Digite o valor de B: "))

        # Exibir os resultados das operações
        print(f"Soma: {soma(a, b)}")
        print(f"Subtração: {subtracao(a, b)}")
        print(f"Multiplicação: {multiplicacao(a, b)}")
        print(f"Divisão: {divisao(a, b)}")
        print('-' * 30)


# Executar o programa
calculadora()