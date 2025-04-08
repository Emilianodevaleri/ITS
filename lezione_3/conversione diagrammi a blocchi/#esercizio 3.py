#esercizio 3
while True:
    nome_corso:str = input("inserire nome corso ")

    max_posti = 100 

   

    while True:
        opzione:str = input("scegliere un'opzione ")

        match opzione:
            case opzione if opzione == "inscrivi":
                if max_posti > 0:
                    max_posti = max_posti - 1
                else:
                    print("non ci sono posti disponibili")

            case opzione if opzione == "annulla":
                if max_posti < 100:
                    max_posti = max_posti + 1

                else:
                    print("tutti i posti sono gia disponibili")

            case opzione if opzione == "visualizza":
                print(max_posti)
                print(100 - max_posti)

            case opzione if opzione == "elimina":
                break

            case opzione if opzione == "esci":
                exit
            
        


