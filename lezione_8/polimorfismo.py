from persona import Persona
from alieno import Alieno

# creare un oggetto p della classe Persona
p: Persona = Persona("Emiliano", "De Valeri", 20)

# visualizzare le informazione dell'ggetto p 
print(p)

# creare un oggetto et della classe Alieno
et: Alieno = Alieno("Andromeda")

# visualizzare le informazioni dell'oggetto et
print(et)

# l'oggetto p invochi il metodo speak()
p.speak()

# invochiamo il metodo speak dall'oggetto et
et.speak()
