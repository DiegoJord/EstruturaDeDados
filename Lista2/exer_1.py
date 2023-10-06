# Crie uma classe chamada “Circulo” que tenha um atributo “raio”. Implemente um método chamado
# “calcular_area” que retorna a área do círculo.

class Circulo:
    def calcular_area(self, raio):
        return 3.14 * (raio * raio)


calc = Circulo()
print(calc.calcular_area(5))