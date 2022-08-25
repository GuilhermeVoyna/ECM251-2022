from os import remove
from item import Item
from carrinho import Carrinho

item1=Item('Carregador','Carrega IpHone e Android',200.0)

item2=Item(
    valor=350.0,
    nome='Stray',
    descricao='Gato.'
)

item3=Item(
    valor=350.0,
    nome='Stray',
    descricao='Gato.'
)

print(item1==item2)
print(item1==item1)
print(item2==item3)

carrinho = Carrinho()

print(f'Tamanho: {carrinho.get_quantidadede_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')

carrinho.adicionar(item1)
carrinho.adicionar(item2)

carrinho.remover(item3)

print(f'Tamanho: {carrinho.get_quantidadede_itens()}')
print(f'Valor: {carrinho.get_valor_total()}')