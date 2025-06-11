def positivinegativi(list_n:list) -> dict:
    positivi:list = []
    negativi:list = []
    dizionario = {"positivi":positivi, "negativi":negativi}
    for n in list_n:
        if n > 0:
            positivi.append(n)
        else:
            negativi.append(n)

    return dizionario

print(positivinegativi([1,-3,5,7,8,-8,5,3,2,-5,7,54,-23,645]))
