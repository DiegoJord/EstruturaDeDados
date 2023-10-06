# Escreva um programa que solicite um número ao usuário e imprima todos os números pares
# de 0 até o número informado.

numero = int(input("Informe um número: "))

print("Números pares de 0 até", numero, ":")

for i in range(0, numero + 1, 2):
    print(i)
