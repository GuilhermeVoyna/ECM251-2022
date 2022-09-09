
from pagamento import Pagamento
from cartoes import Credito

cartao1 = Credito("4349376436367813", "Batman", "1233", "123")
cartao2 = Credito("1111111111111111", "Batman", "1233", "123")
cartao3 = Credito("0000000000000000", "Batman", "1233", "123")
print((cartao1.verifica_credido()))
print((cartao2.verifica_credido()))
print((cartao3.verifica_credido()))