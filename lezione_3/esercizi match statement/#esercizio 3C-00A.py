#esercizio 3C-00
n:int=int(input("inserire il numero di neonati "))

match n:
    case 1:
        print("congratulazioni")
    
    case 2:
        print("Wow! Gemelli!")
    
    case 3:
        print("Wow! Tre!")
    
    case 4:
        print("Mamma mia Quattro! Wow!")
    
    case 5:
        print("incredibile! Cinque!")
    
    case 6:
        print(f"Non ci credo! {n} bambini!")