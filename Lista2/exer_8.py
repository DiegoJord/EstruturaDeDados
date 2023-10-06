# Crie uma classe chamada “Aluno” com atributos “nome” e “notas”. Implemente um método chamado
# “calcular_media” que retorna a média das notas do aluno

class Aluno:
    def calcular_media(self, nome, nota1, nota2, nota3):
        media = (nota1 + nota2 + nota3) / 3
        if media >= 7:
            print(f"Media: {media:.2f}. Aluno: {nome}")
        else:
            print("Reprovado")

        return media


aluno1 = Aluno()
aluno1.calcular_media("Diego Jordânio", 10, 7, 7)
