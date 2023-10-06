# Escreva um programa que recebe cinco notas de um aluno e calcula a média. Em seguida, exiba se o
# aluno foi aprovado (média maior ou igual a 7) ou reprovado (média menor que 7).

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))
nota4 = float(input("Digite sua quarta nota: "))
nota5 = float(input("Digite sua quinta nota: "))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

if (media >= 7):
    print(f"Sua média é {media}, logo está aprovado")

else:
    print(f"Sua média é {media}, logo está reprovado")