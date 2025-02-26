#esercizio 3C-5

user:dict={"nome":input("inserire nome "), "ruolo":input("inserire ruolo "), "età":int(input("inserire età "))}

match user:
    
    case user if user["ruolo"]=="admin":
        print("Accesso completo a tutte le funzionalità.")
    case user if user["ruolo"]=="moderator":
        print("Può gestire i contenuti ma non modificare le impostazioni.")
    case user if user["ruolo"]=="utente" and user["età"] >= 18:
        print("Accesso standard a tutti i servizi.")
    case user if user["ruolo"]=="utente" and user["età"] < 18:
        print("Accesso limitato! Alcune funzionalità sono bloccate.")
    case user if user["ruolo"]=="ospite":
        print("Accesso ristretto! Solo visualizzazione dei contenuti.")
    case _:
        print("Attenzione! Ruolo non riconsciuto! Accesso Negato!")