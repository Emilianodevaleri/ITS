#esercizio 2

nord_sud = int(input("quanti veicoli vengono dalla direzione Nord-Sud "))
est_ovest = int(input("quanti veicoli vengono dalla direzione Est-Ovest "))

soglia:int = 70

if nord_sud > soglia and est_ovest > soglia:
    time_ns = 50
    time_eo = 50
elif nord_sud > soglia:
    time_ns = 60
    time_eo = 40
elif est_ovest > soglia:
    time_ns = 40
    time_eo = 60
else:
    time_ns = (nord_sud / (nord_sud + est_ovest)) * 100
    time_eo = (est_ovest / (nord_sud + est_ovest)) * 100

print(f"il tempo asseganto alla direzione Nord-Sud è {time_ns}")
print(f"il tempo asseganto alla direzione Est-Ovest è {time_eo}")


