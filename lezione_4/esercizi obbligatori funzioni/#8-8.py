#8-8

album:dict = {}
def make_album():
    while True: 
        opzione:str = input('inserire continua per inserire un nuovo album o esci per uscire ')
        if opzione == 'esci':
            break

        elif opzione == 'continua':
            artist_name = input('Inserire nome artista: ')
            album_name = input('Inserire nome album: ')
            album[artist_name] = album_name

        else:
            print('Comando non riconosciuto') 
            continue 

    return print(album) 

make_album()

