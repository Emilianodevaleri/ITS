#conversione di esercizisu diagrammi a blocchi

a:float=float(input("inserire ipotenusa a "))
b:float=float(input("inserire cateto b "))

if a < b:
    print("errore: cateto maggiore dell'ipotenusa")
    
else:
    c=(a**2-b**2)**(1/2)
    print(c)