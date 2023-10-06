# Crie uma função que recebe um vetor de números inteiros e retorna o segundo menor número.
# Certifique-se de que sua função funcione mesmo se houver números duplicados no vetor.

def segundo_menor(vetor):
    if len(vetor) < 2:
        return None

    menor = float('inf')
    segundo_menor = float('inf')

    for num in vetor:
        if num < menor:
            segundo_menor = menor
            menor = num
        elif num < segundo_menor and num != menor:
            segundo_menor = num

    if segundo_menor == float('inf'):
        return None

    return segundo_menor

vetor = [64, 25, 12, 22, 11, 12]

segundo_menor_numero = segundo_menor(vetor)

if segundo_menor_numero is not None:
    print("O segundo menor número é:", segundo_menor_numero)
else:
    print("Não há segundo menor número no vetor.")