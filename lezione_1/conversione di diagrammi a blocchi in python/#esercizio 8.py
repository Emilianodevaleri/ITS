#esercizio 8

soglia = int(input("inserisci soglia "))
cont = 0

while cont != 7:
    n = int(input("inserire numero "))

    if n > soglia:
        print(f"{n} è maggiore di {soglia}")
    
    cont = cont + 1
        