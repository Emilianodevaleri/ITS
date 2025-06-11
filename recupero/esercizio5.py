def moltiplica(listainteri:list):
    N = 1
    for n in listainteri:
        if n < 10:
            N = N * n 

    return N

print(moltiplica([2,59,32,4,7,9,1,245,6]))
