# Crie uma função que aceite um vetor de números inteiros e retorne o terceiro maior número.
# Certifique-se de que sua função funcione mesmo se houver números duplicados
# no vetor.

def terceiro_maior(vetor):

    elementos_unicos = list(set(vetor))

    if len(elementos_unicos) < 3:
        return None

    elementos_unicos.sort(reverse=True)

    return elementos_unicos[2]

vetor = [10, 5, 5, 3, 8, 10, 12, 12]

terceiro_maior_numero = terceiro_maior(vetor)

if terceiro_maior_numero is not None:
    print("O terceiro maior número é:", terceiro_maior_numero)
else:
    print("Não há terceiro maior número no vetor.")