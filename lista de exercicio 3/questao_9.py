# Crie uma calculadora que realiza operações de adição, subtração, multiplicação e divisão, com base
# na escolha do usuário.

def adicao(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Divisão por zero não é permitida."
    return x / y

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Digite o número da operação desejada: ")

if opcao == '1':
    resultado = adicao(numero1, numero2)
    operacao = "adição"
elif opcao == '2':
    resultado = subtracao(numero1, numero2)
    operacao = "subtração"
elif opcao == '3':
    resultado = multiplicacao(numero1, numero2)
    operacao = "multiplicação"
elif opcao == '4':
    resultado = divisao(numero1, numero2)
    operacao = "divisão"
else:
    resultado = "Opção inválida."

if type(resultado) == float:
    print(f"O resultado da {operacao} é: {resultado:.2f}")
else:
    print(resultado)