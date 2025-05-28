from types_voli_aerei import RealGEZ
class città:
    _nome:str
    _abitanti:RealGEZ

    def __init__(self, nome:str, abitanti:RealGEZ) -> None:
        self.set_nome(nome)
        self.set_abitanti(abitanti)

    def nome(self) -> str:
        return self._nome

    def abitanti(self) -> RealGEZ:
        return self._abitanti
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_abitanti(self, a: RealGEZ) -> None:
        self._abitanti = a
       