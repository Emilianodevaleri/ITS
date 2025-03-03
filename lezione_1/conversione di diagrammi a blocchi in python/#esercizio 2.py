#esercizio 2

#ciclo while

max:float = float(input("inserire numero "))
cont:int = 1

while cont < 4:
    n:float = float(input("inserire numero "))
    cont += 1
    if n > max:
        max = n

print(f"il massimo valore è {max}")

#ciclo repeat

max:float = float(input("inserire numero"))
cont:int = 1

while True:
    
    n:float = float(input("inserire numero "))

    if n > max:
        max = n

    cont += 1

    if cont == 4:
        break

print(f"il massimo valore è {max}")

#ciclo for

max:float = float(input("inserire un numero "))

for x in range (3):
    n:float = float(input("inserire un numero "))

    if n > max:
        n = max

print(f"il massimo valore è {max}")
