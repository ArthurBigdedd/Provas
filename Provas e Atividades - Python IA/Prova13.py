class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0.0):
        self._titular = titular
        self._saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado!")
        else:
            print("Erro: O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= 0:
            print("Erro: O valor do saque deve ser positivo.")
        elif valor <= self._saldo:
            self._saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado!")
        else:
            print(f"Erro: Saldo insuficiente (Saldo atual: R$ {self._saldo:.2f}).")

    def exibir_saldo(self):
        print("="*30)
        print(f"TITULAR: {self._titular}")
        print(f"SALDO ATUAL: R$ {self._saldo:.2f}")

# ==========================================================

print("--- Bem-vindo ao Sistema Bancário ---")
nome = input("Digite o nome do titular: ")
saldo_ini = float(input("Digite o saldo inicial: "))

conta = ContaBancaria(nome, saldo_ini)

while True:
    print("="*30)
    print("O que deseja fazer?")
    print("1. Depositar")
    print("2. Sacar")
    print("3. Exibir Saldo")
    print("4. Sair")
    print("="*30)
    opcao = input("Escolha uma das opções acima: ")

    if opcao == '1':
        valor = float(input("Digite o valor para depósito: "))
        conta.depositar(valor)
    
    elif opcao == '2':
        valor = float(input("Digite o valor para saque: "))
        conta.sacar(valor)
        
    elif opcao == '3':
        conta.exibir_saldo()
        
    elif opcao == '4':
        print("Encerrando o sistema. Até logo!")
        break
        
    else:
        print("Opção inválida! Tente novamente.")