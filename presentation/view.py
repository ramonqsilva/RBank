class RBankViewLayer:
    """Responsável pela interface via terminal (CLI)."""
    def __init__(self, service_layer):
        self.service_layer = service_layer

    def iniciar_sistema(self):
        while True:
            print("\n" + "="*45)
            print("💰 RBANK - TERMINAL DO CLIENTE 💰")
            print("="*45)
            
            # Mostra o status atual no topo do menu
            if self.service_layer.conta_atual:
                conta = self.service_layer.conta_atual
                print(f"Cliente: {conta.nome} | RM: {conta.rm}")
                print(f"Endereço: {conta.endereco}")
                print(f"Saldo Disponível: R$ {conta.saldo:.2f}")
            else:
                print("Nenhuma conta selecionada no momento.")
            
            print("-" * 45)
            print("1. Selecionar Conta")
            print("2. Consultar Saldo")
            print("3. Realizar Depósito")
            print("4. Realizar Saque")
            print("5. Atualizar Endereço Cadastral (CEP)")
            print("6. Sair")
            
            opcao = input("\nDigite a opção desejada: ")
            
            if opcao == '1':
                nome = input("Digite o nome completo do titular da conta: ")
                print("\n> " + self.service_layer.selecionar_conta(nome))
                
            elif opcao == '2':
                print("\n> " + self.service_layer.consultar_saldo())
                
            elif opcao == '3':
                try:
                    valor = float(input("Digite o valor para depósito: R$ "))
                    print("\n> " + self.service_layer.realizar_deposito(valor))
                except ValueError:
                    print("\n> Erro: Por favor, digite um número válido.")
                    
            elif opcao == '4':
                try:
                    valor = float(input("Digite o valor para saque: R$ "))
                    print("\n> " + self.service_layer.realizar_saque(valor))
                except ValueError:
                    print("\n> Erro: Por favor, digite um número válido.")
            
            elif opcao == '5':
                cep = input("Digite o CEP (somente números): ")
                print("\nBuscando na base de dados (ViaCEP)...")
                print("> " + self.service_layer.atualizar_endereco_conta(cep))
                    
            elif opcao == '6':
                print("\nEncerrando o sistema RBank...")
                break
            else:
                print("\n> Opção inválida! Tente novamente.")