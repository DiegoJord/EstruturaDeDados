# Faça um programa que leia uma lista de números e retorne a média dos números pares.

numeros = input("Informe uma lista de números separados por espaço: ")


lista_numeros = [int(x) for x in numeros.split()]


numeros_pares = [num for num in lista_numeros if num % 2 == 0]


if numeros_pares:
    media = sum(numeros_pares) / len(numeros_pares)
    print("A média dos números pares é:", media)
else:
    print("Não há números pares na lista.")
