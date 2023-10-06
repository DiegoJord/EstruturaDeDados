# Escreva uma função que gera a sequência de Fibonacci até um determinado número de termos
# especificado pelo usuário.

def fibonacci(n):
    sequencia = []

    if n <= 0:
        return sequencia

    a, b = 0, 1
    sequencia.append(a)

    while len(sequencia) < n:
        a, b = b, a + b
        sequencia.append(a)

    return sequencia

n = int(input("Digite o número de termos desejado na sequência de Fibonacci: "))

resultado = fibonacci(n)

print(f"Sequência de Fibonacci com {n} termos: {resultado}")