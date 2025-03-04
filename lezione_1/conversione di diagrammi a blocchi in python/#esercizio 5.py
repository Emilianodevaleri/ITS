# esercizio 5

n:int = int(input("inserire un  numero intero positivo "))

if n < 2:
    print("il numero non è primo")

div = 2
is_prime:bool = True

while div < n:
    if n%div == 0: 
        is_prime = False
        break
    else:
        div = div + 1
    
if is_prime:
    print("il numero è primo")
else:
    print("il numero non è primo")

