from math import *
class Frazione:
    def __init__(self, numeratore, denominatore):
        self.numeratore = numeratore
        self.denominatore = denominatore

    def value(self) -> float:
        return round(self.numeratore / self.denominatore, 3)
    
    def __str__(self) -> str:
        return f"{self.numeratore} / {self.denominatore}"
    
    def set_numeratore(self, n: int) -> None:
        if isinstance(n, int):
            self.numeratore = n 
        else:
            self.numeratore = 13

    def set_denominatore(self, d: int) -> None:
        if isinstance(d, int):
            self.denominatore = d
        elif d == 0:
            self.denominatore = 5
        else:
            self.denominatore = 5

    def get_numeratore(self) -> int:
        return self.numeratore
    
    def get_denominatore(self) -> int:
        return self.denominatore
    
def mcd(x: int, y: int) -> int:
    divisori_x = []
    divisori_y = []
    fattori_comuni = []
    for n in range(1, x+1):
        
        if x % n == 0: 
            divisori_x.append(n)

    for n in range(1, y+1):
       
        if y % n == 0:
            divisori_y.append(n)

    for n in divisori_x:
        if n in divisori_x and divisori_y:
            fattori_comuni.append(n)
    
    return (fattori_comuni)

print(mcd(12,18))





    




