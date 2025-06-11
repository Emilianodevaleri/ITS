from typing import Self

class Cf(str):

    def __new__(cls, value) -> Self:

        if not value.isalnum() or len(value) != 16:
            raise ValueError("Codice fiscale non valido")
        
        return str.__new__(cls, value)
    

class Anno_isc(float):
   
    def __new__(cls, v: int | float | str | bool | Self) -> Self:
       
        n: float = super().__new__(cls, v)

        if n >= 2000:
            return n

        raise ValueError("inserire un numero plausibile")
    

class Voto:
    v:int

    def __init__(self, v:int):
        if v < 18 or v > 31:
            raise ValueError(f"il voto = {v} deve essere tra 18 e 31")
        
        self.v = v

    def __eq__(self, other):
        return self.v == other.v