class Conta:
    def __init__(self, nome, saldo, limite,):
        self.nome = nome
        self.saldo = saldo
        self.limite = limite

    def saca(self, valor):
        saldoatual = self.saldo - valor
        return saldoatual

    def extrato(self):
        print("Seu saldo atual e de: {} ".format(self.saldo))

    def deposita(self, valor):
        saldoatual = self.saldo + valor
        return saldoatual


