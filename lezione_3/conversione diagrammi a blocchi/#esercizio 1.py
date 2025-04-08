#esercizio 1

max_posti = int(input("inserire numnero di posti "))

liberi:int = max_posti

opzione:str = input("inserire opzione ")


while True:

    match opzione:
        case opzione if opzione == "ingresso":
            if liberi > 0:                    liberi = liberi -1   
            else:
                print("non ci sono posti disponibili")

        case opzione if opzione == "uscita":
            if liberi < max_posti:
                    liberi = liberi -1
            else:
                print("tutti i posti sono già disponibili")

        case opzione if opzione == "stato":
            print(liberi)
            print(max_posti - liberi)

        case opzione if opzione == "esci":
            break
   