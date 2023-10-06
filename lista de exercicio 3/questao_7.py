# Crie uma função que calcula o índice de massa corporal (IMC) de uma pessoa com base em sua altura
# e peso.

def calcular_imc(peso, altura):
    if peso <= 0 or altura <= 0:
        return "Valores inválidos. Peso e altura devem ser positivos."

    imc = peso / (altura ** 2)

    return imc

peso = float(input("Digite seu peso (em quilogramas): "))
altura = float(input("Digite sua altura (em metros): "))

resultado_imc = calcular_imc(peso, altura)

print(f"Seu Índice de Massa Corporal (IMC) é: {resultado_imc:.2f}")