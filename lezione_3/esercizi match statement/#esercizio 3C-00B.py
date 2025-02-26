#esercizio 3C00-B

nome:str=input("inserire il proprio nome ")
gender:str=input("inserire il proprio genere m per maschio e f per femmina")

match gender:
    case "m":
        print(f"nome: {nome} /n genere:maschio")
    case "f":
        print(f"nome:{nome} /n genere:femmina")
    case _:
        print("errore")