# Crie um programa que simule o jogo "Pedra, Papel e Tesoura" entre o usuário e o
# computador. O programa deve solicitar a escolha do usuário e, em seguida, escolher
# aleatóriamente a escolha do computador e determinar o vencedor.

import random

def determinar_vencedor(escolha_usuario, escolha_computador):
    if escolha_usuario == escolha_computador:
        return "Empate"
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
         (escolha_usuario == "papel" and escolha_computador == "pedra") or \
         (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        return "Você venceu!"
    else:
        return "Seu adversário venceu!"

opcoes = ["pedra", "papel", "tesoura"]

print("Escolha: pedra, papel ou tesoura")
escolha_usuario = input("Sua escolha: ").lower()

if escolha_usuario in opcoes:
    escolha_computador = random.choice(opcoes)
    print("Seu adversário escolheu:", escolha_computador)
    resultado = determinar_vencedor(escolha_usuario, escolha_computador)
    print(resultado)
else:
    print("Escolha inválida. Por favor, escolha entre pedra, papel ou tesoura.")
