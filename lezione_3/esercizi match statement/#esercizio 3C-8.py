#esercizio 3C-8

frase:str=input("scrivi una frase ")

match frase:
    case frase if len (frase) %2==1 and frase[-1]=="?":
        print("No")
    case frase if len (frase) %2==0 and frase[-1]=="?":
        print("Si")
    case frase if frase[-1]=="!":
        print("Wow!")
    case _:
        print(f'tu dici "{frase}"')