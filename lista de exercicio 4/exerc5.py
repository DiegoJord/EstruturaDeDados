# Implemente uma função que aceite um vetor de números
# inteiros e remova todos os elementos duplicados, retornando o
# vetor resultante sem duplicatas.

def remover_duplicatas(vetor):

    elementos_unicos = set()

    vetor_sem_duplicatas = []

    for elemento in vetor:
        if elemento not in elementos_unicos:
            elementos_unicos.add(elemento)
            vetor_sem_duplicatas.append(elemento)

    return vetor_sem_duplicatas


vetor = [1, 2, 2, 3, 4, 4, 5, 5, 6]

vetor_sem_duplicatas = remover_duplicatas(vetor)

print("Vetor sem duplicatas:", vetor_sem_duplicatas)