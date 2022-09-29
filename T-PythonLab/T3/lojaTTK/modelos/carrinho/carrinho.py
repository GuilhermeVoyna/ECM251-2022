class Carrinho():
    #Metodo Construtor
    def __init__(self):
        self._itens=[]
    
    def get_valor_total(self):
    
        total =0
        for item in self._itens:
            total+=item.get_valor()
    
        return total

    def get_quantidadede_itens(self):
        return len(self._itens)

    def adicionar(self,item):
        self._itens.append(item)

    def remover(self,item):
        if item in self._itens:
            self._itens.remove(item)
        pass
        