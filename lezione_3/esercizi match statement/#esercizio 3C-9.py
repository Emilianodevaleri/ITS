#esercizio 3C-9

cordinataX:int=int(input("inserire cordinata X "))
cordinataY:int=int(input("inserire cordinata Y "))

punto=(cordinataX,cordinataY)

match punto:
    case (0,0):
        print("il punto (0,0) si trova nell'origine.")
    case (0,cordinataY):
        print(f"il punto {punto} trova sull'asse Y.")
    case (cordinataX,0):
        print(f"il punto {punto} trova sull'asse X.")
    case punto if cordinataX>0 and cordinataY>0:
        print("Il punto si trova nel primo quadrante.")
    case punto if cordinataX<0 and cordinataY>0:
        print("Il punto si trova nel secondo quadrante.")
    case punto if cordinataX<0 and cordinataY<0:
        print("Il punto si trova nel terzo quadrante.")
    case punto if cordinataX>0 and cordinataY<0:
        print("Il punto si trova nel quarto quadrante.")
    