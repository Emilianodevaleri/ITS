#esercizio 6

n = int(input("inserire un numero intero positivo "))

if n%1 == 1 or n < 0:
    print("il numero inserito deve essere intero positivo") 

fattoriale = 1
i = 1

while i != n:
    
    i = i + 1
    fattoriale = fattoriale * i
    

print(f"il fattoriale di {n} è {fattoriale}")

    
    
    


 


