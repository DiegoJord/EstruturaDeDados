# Crie um programa que determine se um número é primo ou não.

def num_primo(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

numero = int(input("Insira um número: "))

if num_primo(numero):
    print(numero, "é um número primo.")
else:
    print(numero, "não é um número primo.")
