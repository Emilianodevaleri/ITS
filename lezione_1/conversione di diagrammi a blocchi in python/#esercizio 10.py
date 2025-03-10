#esercizio 10

r = int(input("inserire reddito "))
m = int(input("inserire media voti "))

if r < 20000 and m > 27:
    print("borsa di studio approvata")

else:
    print("bosra di studio rifiutata (motivo: reddito o media insufficiente)")