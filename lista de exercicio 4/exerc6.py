# Escreva um programa que ordene um vetor de inteiros em ordem decrescente e, em seguida, conte
# quantos números pares e quantos números ímpares existem no vetor ordenado.

def ordenar_decrescente(vetor):

    vetor_ordenado = sorted(vetor, reverse=True)
    return vetor_ordenado

def contar_pares_impares(vetor):
    pares = 0
    impares = 0

    for numero in vetor:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1

    return pares, impares

vetor = [64, 25, 12, 22, 11, 36, 48]

vetor_ordenado = ordenar_decrescente(vetor)
print("Vetor ordenado em ordem decrescente:", vetor_ordenado)

pares, impares = contar_pares_impares(vetor_ordenado)
print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)