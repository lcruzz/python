class ContaBancaria:
    def __init__(self, numero_conta,saldo):
        self.numero_conta = numero_conta
        self.__saldo = saldo

    def depositar (self,valor_deposito):
        self.__saldo += valor_deposito
        return self.__saldo

    def sacar(self,valor_saque):
        if valor_saque <= self.__saldo:
            self.__saldo -= valor_saque
            return self.__saldo
        else:
            print("Saldo insuficiente")

    def acao(self):
        self.numero_da_conta = int(input("Digite o número da conta: "))
        self.__saldo = float(input("Informe o saldo atual da conta: "))
        acao = input("Você deseja fazer um depósito ou um saque? ")
        if acao == "deposito":
            valor_deposito = float(input("Quanto você deseja depositar? "))
            self.__saldo = self.depositar(valor_deposito)
        elif acao == "saque":
            valor_saque = float(input("Quanto você deseja sacar? "))
            self.__saldo = self.sacar(valor_saque)

    def get_saldo(self):
        print(self.__saldo)        

minhaconta = ContaBancaria()
minhaconta.acao()
minhaconta.get_saldo()