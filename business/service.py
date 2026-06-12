class RBankServiceLayer:
    def __init__(self, data_layer, api_layer=None):
        self.data_layer = data_layer
        self.api_layer = api_layer
        self.conta_atual = None

    def selecionar_conta(self, nome):
        conta_encontrada = self.data_layer.buscar_conta_por_nome(nome)
        
        if conta_encontrada:
            self.conta_atual = conta_encontrada
            return f"Sucesso! Conta de {self.conta_atual.nome} (RM: {self.conta_atual.rm}) selecionada."
        else:
            return "Erro: Conta não encontrada no sistema."

    def consultar_saldo(self):
        if not self.conta_atual:
            return "Erro: Nenhuma conta foi selecionada ainda."
        return f"Saldo Disponível: R$ {self.conta_atual.saldo:.2f}"

    def realizar_deposito(self, valor):
        if not self.conta_atual:
            return "Erro: Selecione uma conta primeiro."
            
        if self.conta_atual.depositar(valor):
            return f"Depósito de R$ {valor:.2f} realizado com sucesso!"
        return "Erro: Valor de depósito inválido."

    def realizar_saque(self, valor):
        if not self.conta_atual:
            return "Erro: Selecione uma conta primeiro."
            
        if self.conta_atual.sacar(valor):
            return f"Saque de R$ {valor:.2f} realizado com sucesso!"
        return "Erro: Saldo insuficiente ou valor inválido."

    def atualizar_endereco_conta(self, cep):
        if not self.conta_atual:
            return "Erro: Selecione uma conta primeiro."
            
        if not self.api_layer:
            return "Erro: Módulo de API não configurado."
            
        resultado = self.api_layer.buscar_endereco_por_cep(cep)
        
        if "erro" in resultado:
            return resultado["erro"]
            
        endereco_formatado = f"{resultado.get('logradouro')}, {resultado.get('bairro')} - {resultado.get('localidade')}/{resultado.get('uf')}"
        self.conta_atual.endereco = endereco_formatado 
        
        return "Sucesso: Endereço atualizado."