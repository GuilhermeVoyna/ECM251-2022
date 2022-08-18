from abc import ABC

class Pagamento(ABC):
    @abstractmethod
    def realizar_pagamento(self):
        pass
