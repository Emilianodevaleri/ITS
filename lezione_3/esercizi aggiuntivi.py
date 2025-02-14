'''Esercizio 1
Scrivere un programma che utilizzi un loop for per stampare ogni elemento di una lista.'''
lista = ["penna", "matita", "gomma", "righello"]

for elemento in lista:
    print(elemento)


'''Esercizio 2
Scrivere un programma che utilizzi un loop for per stampare tutti i numeri da 1 a 10.'''

for numero in range(1, 11):
    print(numero)

'''Esercizio 3
Scrivere un programma che utilizzi un loop for per sommare tutti i numeri in una lista.'''

lista = [2, 5, 8, 10]
somma = 0

for numero in lista:
    somma += numero

print("La somma è:", somma)

'''Esercizio 4
Scrivere un programma che utilizzi un loop for per stampare tutti i numeri pari da 1 a 20.'''

for numero in range(2, 21, 2):
    print(numero)

'''Esercizio 5
Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di una stringa.'''

stringa = "ciao a tutti"

for lettera in stringa:
    print(lettera)

'''Esercizio 6
Scrivere un programma che utilizzi un loop for per stampare tutte le chiavi di un dizionario.'''

dizionario = {"nome": "Mario", "cognome": "Rossi", "eta": 30}

for chiave in dizionario:
    print(chiave)

'''Esercizio 7
Scrivere un programma che utilizzi un loop for per stampare tutte le coppie chiave-valore di un dizionario.'''
dizionario = {"nome": "Mario", "cognome": "Rossi", "eta": 30}

for chiave, valore in dizionario.items():
    print(chiave, ":", valore)
'''Esercizio 8
Scrivere un programma che utilizzi un loop for per stampare tutte le lettere di ogni stringa in una lista.'''
lista = ["ciao", "a", "tutti"]

for parola in lista:
    for lettera in parola:
        print(lettera)
'''Esercizio 9
Scrivere un programma che utilizzi un loop for per contare quante volte una lettera compare in una stringa.'''
stringa = "banana"
conta_a = 0

for lettera in stringa:
    if lettera == "a":
        conta_a += 1

print("La lettera a compare", conta_a, "volte.")
'''Esercizio 10
Scrivere un programma che utilizzi un loop for per calcolare la media di una lista di numeri.'''

lista = [4, 6, 8, 10, 2]
somma = 0

for numero in lista:
    somma += numero

media = somma / len(lista)
print("La media è:", media)
