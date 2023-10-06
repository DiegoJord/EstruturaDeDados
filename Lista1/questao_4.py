# Crie um programa que leia uma lista de números e exiba o maior e o menor valor da lista.

numeros = input("Escreva uma lista de números separados por espaço: ")


lista_numeros = [int(x) for x in numeros.split()]


if lista_numeros:
    maior = max(lista_numeros)
    menor = min(lista_numeros)

    print("O maior valor na lista é:", maior)
    print("O menor valor na lista é:", menor)
else:
    print("A lista está vazia.")
