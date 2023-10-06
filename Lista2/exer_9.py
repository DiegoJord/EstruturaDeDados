# Crie uma classe chamada “Triangulo” com atributos “lado1”, “lado2” e “lado3”.
# Implemente um método chamado “calcular_perimetro” que retorna o perímetro do triângulo.

class Triangulo:
    def calcular_perimetro(self, lado1, lado2, lado3):
        perimetro = lado1 + lado2 + lado3
        print(f"Perimetro: {perimetro}")
        return perimetro


triangulo1 = Triangulo()
triangulo1.calcular_perimetro(10, 20, 10)