import random

class Creatura:
    
    def __init__(self, __nome:str):
        self.set_nome(__nome)

    def nome(self):
        return self.__nome
    
    def set_nome(self, nome:str):
        if isinstance(nome, str):
            self.__nome = nome
        else:
            self.__nome = "Creatura Generica"

    def __str__(self):
        return f"Creatura: {self.nome()}"
    
class Alieno(Creatura):

    def __init__(self, __nome):
        super().__init__(__nome)
        self.__set_matricola()
        self.__set_munizioni()
        if __nome == "Robot-" + str(self.matricola()):
            self.set_nome(__nome)
        else:
            print("Attenzione! Tutti gli Alieni devono avere il nome Robot seguito dal numero di matricola! Reimpostazione nome Alieno in Corso!")
            self.set_nome("Robot-" + str(self.matricola()))

    def matricola(self):
        return self.__matricola
    
    def munizioni(self):
        return self.__munizioni
    
    def __set_matricola(self):
        self.__matricola = random.randint(10000, 90000)

    def __set_munizioni(self):
        self.__munizioni = list(x**2 for x in range(0, 16))

    def __str__(self):
        return f"Alieno: {self.nome()}"
    
class Mostro(Creatura):

    def __init__(self, __nome, __urlo_vittoria:str, __gemito_sconfitta:str):
        super().__init__(__nome)
        self.__set_urlo_vittoria(__urlo_vittoria)
        self.__set_gemito_sconfitta(__gemito_sconfitta)
        self.__set_assalto()

    def urlo_vittoria(self):
        return self.__urlo_vittoria
    
    def gemito_sconfitta(self):
        return self.__gemito_sconfitta
    
    def assalto(self):
        return self.__assalto
    
    def __set_urlo_vittoria(self, vittoria:str):
        if isinstance(vittoria, str):
            self.__urlo_vittoria = vittoria
        else:
            self.__urlo_vittoria = "GRAAAHHH"

    def __set_gemito_sconfitta(self, sconfitta:str):
        if isinstance(sconfitta, str):
            self.__gemito_sconfitta = sconfitta
        else:
            self.__gemito_sconfitta = "Uuurghhh"

    def __set_assalto(self):
        self.__assalto = []
        for i in range(15):
            self.__assalto.append(random.randint(1, 100))

    def __str__(self):
        nome:str = self.nome().lower()
        for i in range(1, len(nome), 2):
            nome[i] = nome[i].upper()

        return f"Mostro: {self.nome()}"
        
def pariUguali(a:list[int], b:list[int]):
    c:list[int] = []

    for i in range(len(a)):
        if a[i] % 2 == 0 and b[i] % 2 == 0:
            c.append(1)
        else:
            c.append(0)
    
    return c
    
def combattimento(a:Alieno, m:Mostro):
    if not isinstance(a, Alieno) or not isinstance(m, Mostro):
        print("Combattimento terminato. Avversari non validi")
        return None
    
    c = pariUguali(a.munizioni(), m.assalto())

    conteggio:int = 0

    for i in c:
        if i == 1:
            conteggio += 1

    if conteggio >= 4:
        for i in range(3):
            print(m.urlo_vittoria())

        return m
    else:
        print(m.gemito_sconfitta())
        return a
    
def proclamaVincitore(c: Creatura):
    print(c.nome())

        