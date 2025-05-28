
from types_voli_aerei import RealGEZ
class volo:
    _codice:str
    _durata_min:RealGEZ

    def __init__(self, codice:str, durata_min:RealGEZ) -> None:
        self.set_codice(codice)
        self.set_durata_min(durata_min)

    def codice(self) -> str:
        return self._codice

    def durata_min(self) -> RealGEZ:
        return self._durata_min
    
    def set_codice(self, c: str) -> None:
        self._codice: str = c

    def set_durata_min(self, d: RealGEZ) -> None:
        self._durata_min = d
       