#2
def compoundInterest(m:int, t:int):
    m = 1.005 * m
    
    if t==0:
        return m
    

    return compoundInterest(m, t - 1)


print(compoundInterest(1,6))
    