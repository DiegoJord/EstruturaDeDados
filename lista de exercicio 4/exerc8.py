# Crie uma função que receba um vetor de números inteiros e retorne a mediana, ou seja, o valor
# do meio quando o vetor é ordenado. Certifique-se de que sua função funcione para
# vetores com um número ímpar de elementos.

def calcular_mediana(vetor):

    vetor_ordenado = sorted(vetor)

    n = len(vetor_ordenado)

    if n % 2 == 1:
        mediana = vetor_ordenado[n // 2]
    else:
        meio1 = vetor_ordenado[(n - 1) // 2]
        meio2 = vetor_ordenado[n // 2]
        mediana = (meio1 + meio2) / 2

    return mediana


vetor = [10, 5, 3, 8, 12]

mediana = calcular_mediana(vetor)

print("A mediana é:", mediana)