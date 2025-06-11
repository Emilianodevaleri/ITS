class Contactanager:
    def __init__(self,contacts:dict[str,list[str]]):
        self.contacts = contacts

    def create_contact(self,name:str,phone_numbers:list[str]):
        D1:dict = {}
        if name in self.contacts:
            print("Errore: il contatto esiste già")
        else:
            self.contacts[name] = [phone_numbers]
            D1[name] = [phone_numbers]
        return D1

    def add_phone_number(self,contact_name: str,phone_number:str):
        D2:dict = {}
        if contact_name not in self.contacts:
            print("Errore: il contatto non esiste")
        elif phone_number in self.contacts:
            print("Errore il numero di telefono esiste già")
        else:
            self.contacts[contact_name] = [phone_number]
            D2[contact_name] = [phone_number]
        
        return D2
    
    #def remove_phone_number(self, contact_name:str, phone_number)
    
        
    




