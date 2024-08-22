## ejemplo de cuenta Bancaria
class CuentaBanco:
    def __init__(self,saldo_base):
        self.__saldo = saldo_base

    def depositar(self, valor):
        self.__saldo += valor
        return self.__saldo

    def retirar(self, valor):
        self.__saldo -= valor
        return self.__saldo

    def obtener_saldo(self):
        return self.__saldo


#crea una intancia de mi cuenta
mi_cuenta = CuentaBanco(100)
print(mi_cuenta.obtener_saldo())

mi_cuenta.depositar(50)
print(mi_cuenta.obtener_saldo())

###esto es errro
#mi_cuenta.__saldo
mi_cuenta.retirar(80)
print(mi_cuenta.obtener_saldo())












