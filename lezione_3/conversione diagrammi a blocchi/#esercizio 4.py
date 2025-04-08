#esercizio 4

n_tutor:int = 10

attesa:int = 0

while True:
    studente:str = input("inserire studente ")

    if n_tutor > 0:
        n_tutor = n_tutor - 1
        print("tutor assegnato con successo")
    else:
        attesa = attesa + 1
        print("studente in attesa")
    if n_tutor == 0 and attesa > 50:
        break
    else:
        None