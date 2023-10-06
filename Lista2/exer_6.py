# Crie uma classe chamada “Produto” com atributos “nome”, “preco” e “quantidade”. Implemente um
# método chamado “calcular_total” que retorna o valor total do produto (preço * quantidade).

class Produto:
    def calcular_total(self, nome, preco, quantidade):
        valor_total = preco * quantidade
        print(f"Você comprou {nome}. Por R${preco} e {quantidade} unidades. Pagou no total R${valor_total}")
        return valor_total


produto1 = Produto()
produto1.calcular_total("Bananas", 0.50, 30)
