class Alieno:
    '''
    di un alieno ci interessa sapere la galassia di provenienza 
    self.galaxy:str
    '''

    #inizializzare un oggetto della classe alieno
    def __init__(self, galaxy:str):
        self.setGalaxy(galaxy)

    def setGalaxy(self, galaxy:str) -> None:
        if galaxy:
            self.galaxy = galaxy
        else:
            print("errore! La galassia di provenienza non può essere una stringa vuota")

    def getGalaxy(self) -> str:
        return self.galaxy 
    
    def speak(self) -> None:
        print("\nfhruhxmncrs1\n")

    def __str__(self) ->str:
        return f"\nAlieno proveniente dalla galassia {self.getGalaxy()}!\n"