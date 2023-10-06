# Crie uma classe chamada “Pessoa” com atributos “nome” e “idade”. Implemente um método
# chamado “falar” que imprime uma mensagem com o nome da pessoa

class Pessoa:
    def falar(self, nome, idade):
        print(f"Olá, {nome}. Você tem mesmo {idade} anos?")

falar = Pessoa()
falar.falar("Diego", 26)