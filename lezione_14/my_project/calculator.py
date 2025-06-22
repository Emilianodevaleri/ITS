class Calculator:

    def __init__(self, a: int, b: int):
        self.a = a 
        self.b = b

    def addiction(self) -> int:
        return int(self.a + self.b)
    
    def subcraction(self) -> int:
        return int(self.a - self.b) 
    
    def multiplcation(self) -> int:
        return int(self.a * self.b) 
    
    def division(self) -> int:
        if self.b == 0:
            raise ValueError("divide by zero")
        return round(self.a / self.b) 
