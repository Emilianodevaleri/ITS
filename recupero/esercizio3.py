def prezzi(dizio:dict) -> dict:
    newdizio = {}
    for key,value in dizio.items():
        
        if value < 50:
            value2 = value + value * 10 / 100
            round(value2, 2)
            
            newdizio[key] = [value2]

    print(newdizio)

prezzi({"pera":3.50,"gambero":19, "cavallo":51})