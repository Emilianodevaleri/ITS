#esercizio 3C-4

animale:str= input("inserire un animale ")

Mammiferi:list=["cane", "gatto", "cavallo", "elefante", "leone"]
Rettili:list=["serpente", "lucertola", "tartaruga", "coccodrillo"]
Uccelli:list=["aquila", "pappagallo", "gufo", "falco"]
Pesci:list= ["squalo", "trota", "salmone", "carpa"]

match animale:
    case animale if animale in Mammiferi:
        print(f"{animale} appartiene alla categoria Mammiferi")
    case animale if animale in Rettili:
        print(f"{animale} appartiene alla categoria Rettili")
    case animale if animale in Uccelli:
        print(f"{animale} appartiene alla categoria Uccelli")
    case animale if animale in Pesci:
        print(f"{animale} appartiene alla categoria Pesci")
    case _:
        print(f"Non so dire in quale categoria classificare l'animale {animale}!")