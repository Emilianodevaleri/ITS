from datetime import date
from mytypes import RealGEZ
import dipartimento

from coinvolto import *

class Impiegato:
    _nome: str # noto alla nascita
    _cognome: str # noto alla nascita
    _nascita: date # <<immutable>>, noto alla nascita
    _stipendio: RealGEZ # noto alla nascita
    


    def __init__(self, nome: str, cognome: str, nascita: date, stipendio: RealGEZ, afferenza: dipartimento, direzione: dipartimento) -> None:
        self.set_nome(nome)
        self.set_cognome(cognome)
        self._nascita = nascita
        self.set_stipendio(stipendio)
        self.set_afferenza(afferenza)
        self.set_direzione(direzione)
        self._link_coinvolti = set[coinvolto]()

     

    def nome(self) -> str:
        return self._nome

    def cognome(self) -> str:
        return self._cognome

    def nascita(self) -> date:
        return self._nascita

    def stipendio(self) -> RealGEZ:
        return self._stipendio
    
    def afferenza(self) -> dipartimento:
        return self._afferenza
    
    def direzione(self) -> dipartimento:
        return self._direzione

    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_cognome(self, c: str) -> None:
        self._cognome: str = c

    def set_stipendio(self, s: RealGEZ) -> None:
        self._stipendio = s

    def set_afferenza(self, a: dipartimento) -> None:
        self._afferenza = a

    def set_direzione(self, d: dipartimento) -> None:
        self._direzione = d


    def add_link_coinvolto(self, l):
        if isinstance(l, coinvolto):
            self._link_coinvolti.add(l)

    def get_link_coinvolti(self) -> set[coinvolto]:
        return self._link_coinvolti
