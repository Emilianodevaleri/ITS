def blackjack_hand_total(cards: list[int]) -> int:
    v=0
    asso:bool = False
    for i in cards:
        if i == 11:
            asso = True
        v += i
        if v > 21 and asso == True:
            v -= 10
            
    return v




cards = [2,11,9]
print(blackjack_hand_total(cards))