
#la lepre e la tartaruga

import random

t_pos = 0
l_pos = 0

def posizioni():
    percorso:list = ["_"] *70
    percorso[t_pos] = "T"
    percorso[l_pos] = "L"
    if t_pos==l_pos:
        percorso[l_pos] = "OUCH"
    print()
    




def tart_pos():
    t = random.randint(1,10)
    if 1 <= t <= 5:
        t_pos += 3
    elif 6 <= t <= 7:
        t_pos -= 6
    elif 8 <= t <= 10:
        t_pos += 1







