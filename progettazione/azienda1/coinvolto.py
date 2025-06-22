from impiegato import Impiegato
from progetto import progetto

class coinvolto:

    @classmethod
    def add(cls, impiegato: Impiegato, progetto: progetto) -> None:

        l = cls._link(impiegato, progetto)
        impiegato.add_link_coinvolto(l)
        progetto.add_link_coinvolto(l)

    class _link:

        _impiegato: Impiegato
        _progetto: progetto

        def __init__(self, impiegato: Impiegato, progetto: progetto) -> None:

            self._progetto = progetto
            self._impiegato = impiegato

        def impiegato(self) -> Impiegato:
            return self._impiegato

        def progetto(self) -> progetto:
            return self._progetto