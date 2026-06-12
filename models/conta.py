class Conta:
    """Entidade central do sistema bancário."""
    def __init__(self, nome, rm, saldo_inicial=0.0):
        self.nome = nome
        self.rm = rm
        self.saldo = saldo_inicial
        self.endereco = "Endereço não cadastrado"

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return True
        return False

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return True
        return False