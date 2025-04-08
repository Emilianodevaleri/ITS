def somma_elementi(x: list[int], y: list[int]) -> list[int]:
    
    i=0
    new_list=[]
    while i< len(x):
        z = x[i] + y[i]
        new_list.append(z)
        i+=1
    return new_list    
    
