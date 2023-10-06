# Escreva um programa que leia uma lista de nomes e retorne
# uma nova lista com apenas os nomes que começam com a letra "A".

nomes = input("Escreva uma lista de nomes separados por espaço: ")

lista_nomes = nomes.split()

nomes_com_a = [nome for nome in lista_nomes if nome.startswith('A') or nome.startswith('a')]

print("Nomes que começam com a letra 'A':")
for nome in nomes_com_a:
    print(nome)
