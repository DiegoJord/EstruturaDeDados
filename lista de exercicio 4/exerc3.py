# Escreva um programa que encontre o elemento máximo em um vetor de inteiros
# não ordenado sem usar a função `max()`. Em seguida, encontre o elemento mínimo
# sem usar a função `min()`.

def encontrar_maximo_minimo(vetor):

    if not vetor:
        return None, None

    maximo = vetor[0]  # Inicializa o máximo com o primeiro elemento
    minimo = vetor[0]  # Inicializa o mínimo com o primeiro elemento

    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento
        elif elemento < minimo:
            minimo = elemento

    return maximo, minimo

vetor = [64, 25, 12, 22, 11]

maximo, minimo = encontrar_maximo_minimo(vetor)

if maximo is not None and minimo is not None:
    print("Elemento máximo:", maximo)
    print("Elemento mínimo:", minimo)
else:
    print("O vetor está vazio.")