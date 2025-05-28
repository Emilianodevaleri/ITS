

from typing import Self



class RealGEZ(float):

    def __new__(cls, v: int | float | str | bool | Self) -> Self:

        n: float = super().__new__(cls, v)

        if n >= 0:
            return n

        raise ValueError(f"Il numero inserito {v} è negativo!")
    

class RealG19(float):
   
    def __new__(cls, v: int | float | str | bool | Self) -> Self:
       
        n: float = super().__new__(cls, v)

        if n >= 1900:
            return n

        raise ValueError("inserire un numero plausibile")