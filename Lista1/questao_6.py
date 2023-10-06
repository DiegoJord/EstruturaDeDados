# Escreva um programa que peça um número inteiro positivo ao usuário e calcule o
# fatorial desse número.

numero = int(input("Escreva um número inteiro positivo: "))


if numero < 0:
    print("O número deve ser positivo.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i
    print(f"O fatorial de {numero} é {fatorial}.")
