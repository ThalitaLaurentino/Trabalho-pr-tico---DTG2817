saida = ''

def adicao(a, b):
    return a + b

def subracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    return a / b

def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao == 'soma':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao == 'subtração':
        resultado = subracao(num1, num2)
    elif operacao == '*' or operacao == 'multiplicação':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao == 'divisão':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

while saida.lower() != 'n':
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação desejada (+, -, *, / ou nome da operação como soma, subtração, multiplicação, divisão): ").lower()
        
        resultado = calculadora(num1, num2, operacao)
        print(f"Resultado da operação: {resultado}")
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")
    saida = input("Deseja continuar? (S/N): ").lower()

print("Programa encerrado.")
