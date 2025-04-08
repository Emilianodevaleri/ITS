
import math

def safe_sqrt(number):
    
    if number < 0:
        raise ValueError(f"the number can't be negative: ({number})")
    else:
        x = math.sqrt(number)
        print(x)
        


safe_sqrt(9)

    
