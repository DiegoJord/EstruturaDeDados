# Crie uma classe chamada “ContaBancaria” que tenha atributos “saldo” e “titular”. Implemente
# métodos “depositar” e “sacar” para manipular o saldo.

class ContaBancaria:
    def depositar(saldo, titular):
        print(f"Seu saldo é de {saldo}.")
        return saldo, titular

    def sacar(sacar, saldo, titular):
        saldo = saldo - sacar
        print(f"Voce sacou {sacar}.")
        print(f"Seu novo saldo é de {saldo}.")
        return sacar, saldo, titular


conta1 = ContaBancaria
conta1.depositar(1000, "Diego")
conta1.sacar(300, 1000, "Diego")