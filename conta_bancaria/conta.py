class ContaBancaria():
    def __init__(self,numeroConta:int, nomeCliente:str, tipoConta:str):
        self.numeroConta = numeroConta
        self.saldo = 0
        self.statusConta = False
        self.nomeCliente = nomeCliente
        self.tipoConta = tipoConta
        self.limite = 0
    def depositar(self, valor):
       if self.statusConta == True:
            if valor > 0:
                self.saldo += valor
                print(f'Deposito de {valor} realizado com sucesso')
                print(f'O saldo de {self.nomeCliente} agora é {self.saldo}')
            else:
                print(f'Você precisa depositar alguma quantia.')
       else:
           print('Não foi possível depositar, a conta está inativa')
    def sacar(self, valor):
       if self.statusConta == True:
            if valor > 0 and self.saldo >= valor:
                self.saldo -= valor
                print(f'Saque de {valor} realizado com sucesso')
                print(f'O saldo de {self.nomeCliente} agora é {self.saldo}')
            elif valor > self.saldo:
                print(f'Saldo insuficiente na conta')
            else:
                print(f'Valor inválido para saque')
       else:
           print('Não foi possível realizar o saque, A conta está inativa.')
    def verificarSaldo(self):
        if self.statusConta == True:
            print(f'Saldo atual : {self.saldo}')
        else:
            print('Não é possivél ver o saldo pois a conta está inativa.')

    def ativarConta(self):
        if self.statusConta == False:
            self.statusConta = True
            print('Conta ativada com sucesso')
        else:
            print('Não foi possivel realizar essa ação, pois a conta ja esta ativa.')

    def desativarConta(self):
        if self.statusConta == True and self.saldo == 0:
            self.statusConta = False
            print('Conta desativada')
        else:
            print('Não foi possível realizar essa ação. Verifique se a conta ja esta desativada ou se o saldo esta zerado.')