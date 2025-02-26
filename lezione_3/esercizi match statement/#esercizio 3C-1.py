#esercizio 3C-1
voto:int=int(input("inserire il voto "))
match voto:
    case 10:
        print("Eccellente")
    case voto if voto==8 or voto==9:
        print("Molto buono")
    case voto if voto==7 or voto==6:
        print("sufficiente")
    case voto if voto==5 or voto==4:
        print("insufficiente")
    case voto if voto==3 or voto==2 or voto==1:
        print("gravemente insufficiente")
    case _:
        print("Voto non valido")