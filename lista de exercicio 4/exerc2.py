# Escreva uma função em Python para ordenar um vetor de inteiros, ele deve receber um
# parâmetro que serve como chave para realizar a ordenação crescente ou decrescente.

def ordenar_vetor(vetor, crescente=True):

    vetor_ordenado = sorted(vetor, reverse=not crescente)
    return vetor_ordenado

vetor = [64, 25, 12, 22, 11]

vetor_crescente = ordenar_vetor(vetor)
print("Vetor ordenado crescente:", vetor_crescente)

vetor_decrescente = ordenar_vetor(vetor, crescente=False)
print("Vetor ordenado decrescente:", vetor_decrescente)