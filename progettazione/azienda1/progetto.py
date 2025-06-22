from types_azienda1 import *

from coinvolto import *

class progetto:
    _nome: str
    _budget: RealGEZ
    

    def __init__(self, nome: str, budget: RealGEZ):
        self.set_nome(nome)
        self.set_budget(budget)
        self._link_coinvolti = set[coinvolto] ()

    def nome(self) -> str:
        return self._nome
    
    def budget(self) -> RealGEZ:
        return self._budget
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_budget(self, b: RealGEZ) -> None:
        self._budget: RealGEZ = b


    def add_link_coinvolto(self, l):
        if isinstance(l, coinvolto):
            self._link_coinvolti.add(l)

    def get_link_coinvolti(self) -> set[coinvolto]:
        return self._link_coinvolti