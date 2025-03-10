#esercizio 7

pari:int = 0
dispari:int = 0
cont:int = 0

while cont != 10:
    n = int(input("inserire un numero "))
    
    if n%2==0:
        pari = pari +1
    else:
        dispari = dispari + 1

    cont = cont + 1

print(f"i numeri pari sono {pari}, i numeri dispari sono {dispari}")
