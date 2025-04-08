def even_odd_pattern(numbers:list[int]) -> list[int]:
    pari= []
    dispari=[]
    for i in numbers:
        
        if i %2==0:
            pari.append(i)
        elif i %2!=0:
            dispari.append(i)

            
    return pari + dispari
print(even_odd_pattern([3, 6, 1, 8, 4, 7]))