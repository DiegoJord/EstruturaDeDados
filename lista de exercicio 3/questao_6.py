# Escreva um programa que recebe uma string e conta a quantidade de vogais (a, e, i, o, u) presentes
# nela.

string = input("Digite uma string: ")

string = string.lower()

contador_vogais = 0

vogais = "aeiou"

for caractere in string:
    if caractere in vogais:
        contador_vogais += 1

print(f"A quantidade de vogais na string é: {contador_vogais}")