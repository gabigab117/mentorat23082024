# 1. Polymorphisme d'héritage

class Animal:
    def faire_son(self):
        pass

class Chien(Animal):
    def faire_son(self):
        return "Woof!"

class Chat(Animal):
    def faire_son(self):
        return "Meow!"

# Pour illustrer le concept, fonction polymorphique
def faire_parler_animal(animal):
    print(animal.faire_son())

# Utilisation
mon_chien = Chien()
mon_chat = Chat()

faire_parler_animal(mon_chien)
faire_parler_animal(mon_chat)


# 2. Polymorphisme mais sans héritage

## Si ça marche comme un canard et ça cancane comme un canard, alors ça doit être un canard (duck typing)
## Pas besoin de spécifier le type d'objet, nos objets ont la méthode voler
## Méthodes communes
## Fonction polymorphique
## faire_voler essaye d'appeler la méthode voler

class Canard:
    def voler(self):
        return "Je vole comme un canard"

class Avion:
    def voler(self):
        return "Je vole comme un avion"

def faire_voler(objet_volant):
    print(objet_volant.voler())

canard = Canard()
avion = Avion()

faire_voler(canard)
faire_voler(avion)
