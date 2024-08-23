class Voiture:
    nombre_de_voitures = 0  # Attribut de classe, partage par toutes les instances
    attribut_classe = "Attribut classe"

    def __init__(self, marque, modele, annee):  # Constructeur de classe
        self.marque = marque  # Attribut d'instance
        self.modele = modele
        self.annee = annee
        self._kilometrage = 0  # Attribut privé
        Voiture.nombre_de_voitures += 1

    def __str__(self):  # Représentation lisible de l'objet sous forme de str, lorsqu'on fait print() ou str()
        return f"{self.marque} {self.modele} ({self.annee})"

    def __repr__(self):  # Représenter l'objet pour les dev (pour le debug par ex)
        return f"Voiture(marque='{self.marque}', modele='{self.modele}', annee='{self.annee}')"

    def rouler(self, distance):
        self._kilometrage += distance
        print(f"La voiture a parcouru {distance} km.")

    def obtenir_kilometrage(self):
        # https://www.docstring.fr/accompagnement/questions/894/
        return self._kilometrage

    @staticmethod
    def convertir_miles_en_km(miles):  # Pas accès à self, peut etre appelée sur la classe. Pour certains à éviter
        return miles * 1.60934

    @classmethod
    def depuis_chaine(cls, chaine):  # la classe en premier argument. Ex, méthode alternative de construction, depuis une str
        marque, modele, annee = chaine.split(',')
        return cls(marque, modele, int(annee))

    @classmethod
    def voiture_actuelle(cls): # Création d'une instance avec voiture récente
        return cls("Renault", "Megane", 2024)

    def afficher_marque(self):
        return self.marque


class VoitureElectrique(Voiture):
    def __init__(self, marque, modele, annee, capacite_batterie):
        super().__init__(marque, modele, annee)
        self.capacite_batterie = capacite_batterie

    def __str__(self):
        return f"{super().__str__()} - Batterie: {self.capacite_batterie} kWh"

    def rouler(self, distance):  # Polymorphisme
        super().rouler(distance)
        print("Voiture électrique en mouvement silencieux.")


# Hértage permet de réutiliser le code, hiérarchie
# Polymorphisme : utiliser des objets de différentes classes de manière uniforme. Même interface, comportement différent


print("Voiture 1")
voiture_1 = Voiture("Peugeot", "208", "2009")
print(voiture_1.nombre_de_voitures)
print(voiture_1.marque)
print(voiture_1.attribut_classe)


print("\nVoiture 2")
voiture_2 = Voiture("Renault", "MRS", "2012")
print(voiture_2.nombre_de_voitures)
print(voiture_2.marque)
print(voiture_2.attribut_classe)
voiture_2.attribut_classe = "Attribut d'instance"  # Attribut d'instance dans ce cas !
print(voiture_2.attribut_classe)
print(voiture_2.__class__.attribut_classe)


print("\nSelf")
print(voiture_1.afficher_marque())
print(Voiture.afficher_marque(voiture_1))


# print("\nVoiture 3")
# voiture_3 = eval(repr(voiture_1))
# print(voiture_3)
