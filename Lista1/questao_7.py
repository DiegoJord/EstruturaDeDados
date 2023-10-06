# Crie um programa que imprima a sequencia de Fibonacci até um valor inserido pelo usuário.

def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

limite = int(input("Insira um valor limite para a sequência de Fibonacci: "))

fibonacci_seq = fibonacci_sequence(limite)
print("Sequência de Fibonacci até", limite, ":")
print(fibonacci_seq)
