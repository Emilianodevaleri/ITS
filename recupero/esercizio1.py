def tupladict(listat:list[tuple]) -> dict:
    dict = {}
    for key,value in listat:
        if key in dict:
            dict[key] += value
        else:
            dict[key] = value
    return dict


listat = [("a",1),("b",2),("c",3)]
print(tupladict(listat))

