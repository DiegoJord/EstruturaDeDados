# Crie uma classe chamada “Funcionario” com atributos “nome”, “salario” e “cargo”.
# Implemente um método chamado “aumentar_salario” que recebe um valor percentual
# de aumento e atualiza o salário do funcionário.

class Funcionario:
    def aumentar_salario(self, nome, salario, cargo):
        aumento = salario * 0.10
        novo_salario = salario + aumento
        print(f"{nome}, seu salario de {salario} foi aumentado em {aumento}, ficando assim com novo salario de {novo_salario}")

func1 = Funcionario()
func1.aumentar_salario("Larissa", 3200, "Analista")