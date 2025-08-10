class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        pass
        self._saldo += valor

    def sacar(self, valor):
        pass



conta = Conta(100)
conta.depositar(100)
print(conta._saldo)  # Acesso direto ao atributo protegido, não recomendado