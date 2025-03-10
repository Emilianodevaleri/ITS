#esercizio 9

nome:str = input("inserire nome venditore ")
vendite = int(input("inserire totale vendite "))

max_nome:str = nome
max:int = vendite
min_nome:str = nome
min:int = vendite

cont:int = 0

while cont != 19:
    new_nome:str = input("inserire un nuovo venditore ")
    new_vendite = int(input("inserire il totale vendite del nuovo venditore "))

    if new_vendite > max:
        max_nome = new_nome
        max = new_vendite

    elif new_vendite < min:
        min_nome = new_nome
        min = new_vendite

    cont = cont + 1

print(max_nome, max)
print(min_nome, min)
