# Crie uma classe chamada “Retangulo” que tenha atributos “base” e “altura”. Implemente um método
# chamado “calcular_area” que retorna a área do retângulo

class Retangulo:
    def calcular_area(self, base, altura):
        area = base * altura
        return area


retangulo1 = Retangulo()
print(retangulo1.calcular_area(30, 40))
