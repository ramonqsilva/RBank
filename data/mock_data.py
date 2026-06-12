from models.conta import Conta

class MockDataLayer:
    def __init__(self):
        self.contas_salvas = [
            Conta("Ramon Queiroz e Silva", "24213522", 1000.0),
            Conta("Sara Gomes de Paula", "23213611", 2000.0),
        ]

    def buscar_conta_por_nome(self, nome_buscado):
        for conta in self.contas_salvas:
            if conta.nome.lower() == nome_buscado.lower():
                return conta
        return None