# README: Manipulation de Dates, POO et Polymorphisme en Python

Ce projet illustre l'utilisation de la bibliothèque `datetime`, les concepts de Programmation Orientée Objet (POO) et le polymorphisme en Python.

## 1. Manipulation de Dates avec `datetime`

Le module `datetime` est utilisé pour travailler avec les dates et les heures en Python.

### Fonctionnalités principales :
- Création d'objets `date`, `time` et `datetime`
- Formatage et parsing de dates
- Calculs et comparaisons de dates
- Gestion des fuseaux horaires

### Exemples d'utilisation :
```python
import datetime

# Créer une date
date = datetime.date(2024, 8, 18)

# Formater une date
date_formatee = date.strftime("%d/%m/%Y")

# Parser une chaîne en date
date_parsee = datetime.datetime.strptime("18/08/2024", "%d/%m/%Y")

# Calculs avec timedelta
delta = datetime.timedelta(days=7)
nouvelle_date = date + delta
```

## 2. Programmation Orientée Objet (POO)

La POO est un paradigme de programmation basé sur le concept d'objets contenant des données et du code.

### Concepts clés démontrés :
- Classes et objets
- Attributs et méthodes
- Héritage
- Méthodes spéciales (`__init__`, `__str__`, `__repr__`)
- Méthodes statiques et de classe

### Exemple de classe :
```python
class Voiture:
    nombre_de_voitures = 0  # Attribut de classe

    def __init__(self, marque, modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        Voiture.nombre_de_voitures += 1

    def __str__(self):
        return f"{self.marque} {self.modele} ({self.annee})"

    @classmethod
    def voiture_actuelle(cls):
        return cls("Renault", "Megane", 2024)
```

## 3. Polymorphisme

Le polymorphisme permet à des objets de différentes classes d'être traités de manière uniforme.

### Types de polymorphisme démontrés :
1. Polymorphisme d'héritage
2. Polymorphisme sans héritage (duck typing)

### Exemple de polymorphisme :
```python
class Animal:
    def faire_son(self):
        pass

class Chien(Animal):
    def faire_son(self):
        return "Woof!"

class Chat(Animal):
    def faire_son(self):
        return "Meow!"

def faire_parler_animal(animal):
    print(animal.faire_son())

# Utilisation
mon_chien = Chien()
mon_chat = Chat()

faire_parler_animal(mon_chien)  # Affiche: Woof!
faire_parler_animal(mon_chat)   # Affiche: Meow!
```

Ce README fournit une vue d'ensemble des concepts clés abordés dans le code. Pour plus de détails, référez-vous aux commentaires dans le code source.
