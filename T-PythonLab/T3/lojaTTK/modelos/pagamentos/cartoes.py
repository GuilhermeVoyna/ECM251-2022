from re import T
from pagamento import Pagamento

class Cartao(Pagamento):
    def __init__(self, numero, titular, validade, cvv):
        self._numero = numero
        self._titular = titular
        self._cvv = cvv
        self._validade = validade

    def get_titular(self):
        return self._titular
    def get_validade(self):
        return self._validade
    def get_final(self):
        return self._numero[len(self._numero)-4:]

class Debito(Cartao):
    def __init__(self, numero, titular, validade, cvv):
        super().__init__(numero, titular, validade, cvv)
    def realizar_pagamento(self):
        return True

class Credito(Cartao):
    def __init__(self, numero, titular, validade, cvv):
        super().__init__(numero, titular, validade, cvv)
    def realizar_pagamento(self):
        
        return True

    def verifica_credido(self):

        sumImp = 0
        sumPar = 0
        count = 0
        if self._numero=="0000000000000000":
            return False

        if len(self._numero)==16: 
          imp=[1,3,5,7,9,11,13,15]
          par=[0,2,4,6,8,10,12,14]

          for i in range(8):
            sumImp=int(self._numero[imp[i]])+sumImp
            sumPar=int(self._numero[par[i]])+sumPar
          for i in range(8): 
            if  int(self._numero[par[i]]) > 5 :
                count+=1
        if ((sumImp+2*sumPar)+count )%10==0 and len(self._numero)==16:
            return True
        
        return False