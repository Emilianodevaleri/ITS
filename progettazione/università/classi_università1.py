from types_università1 import Cf
from types_università1 import *
import datetime


class Corsi:
    def __init__(self, nome:str, codice:str, ore_lezione:int ):
        self.set_nome(nome)
        self.set_codice(codice)
        self.set_ore_lezione(ore_lezione)

    def nome(self) -> str:
        return self._nome

    def codice(self) -> str:
        return self._codice
    
    def ore_lezione(self) -> int:
        return self._ore_lezione
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_codice(self, c: str) -> None:
        self._codice: str = c

    def set_ore_lezione(self, o: int) -> None:
        self._ore_lezione: int = o

class Facoltà:
    def __init__(self, nome: str, tipo: str):
        self.set_nome(nome)
        self.set_tipo(tipo)

    def nome(self) -> str:
        return self._nome
    
    def tipo(self) -> str:
        return self._tipo
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_tipo(self, t: str) -> None:
        self._tipo: str = t


class Studenti:
    def __init__(self, nome:str, codice_fiscale:Cf, num_matricola:str, data_nascita:datetime.date, anno_inscrizione:Anno_isc, iscrizione: Facoltà):
        self.set_nome(nome)
        self.set_codice_fiscale(codice_fiscale)
        self.num_matricola = num_matricola
        self.data_nascita = data_nascita
        self.anno_inscrizione = anno_inscrizione
        self.iscrizione = iscrizione

    def nome(self) -> str:
        return self._nome

    def codice_fiscale(self) -> Cf:
        return self._codice_fiscale
    
    def num_matricola(self) -> str:
        return self.num_matricola
    
    def data_nascita(self) -> datetime.date:
        return self.data_nascita

    def anno_inscrizione(self) -> Anno_isc:
        return self.anno_inscrizione
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_codice_fiscale(self, cf: Cf) -> None:
        self._codice_fiscale: Cf = cf
    
    def inscrizione(self) -> Facoltà:
        return self.inscrizione
    

class Professori:
    def __init__(self, nome: str, cod_fiscale: Cf, data_nascita: datetime.date):
        self.set_nome(nome)
        self.set_cod_fiscale(cod_fiscale)
        self.data_nascita = data_nascita
    
    def nome(self) -> str:
        return self._nome

    def cod_fiscale(self) -> Cf:
        return self._cod_fiscale
    
    def data_nascita(self) -> datetime.date:
        return self._data_nascita
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n

    def set_cod_fiscale(self, cf: Cf) -> None:
        self._cod_fiscale: Cf = cf
    
class Corso_superato:
    def __init__(self, voto: Voto):
        self.voto = voto

    def voto(self) -> Voto:
        return self.voto
    
class Città:
    def __init__(self, nome: str):
        self.set_nome(nome)

    def nome(self) -> str:
        return self._nome
    
    def set_nome(self, n: str) -> None:
        self._nome: str = n