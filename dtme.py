# https://strftime.org/
import datetime

# 1. Objet date
print("1. Objet date")
aujourd_hui = datetime.date.today()
print(f"Date d'aujourd'hui : {aujourd_hui}")
date_specifique = datetime.date(2024, 8, 18)
print(f"Date spécifique : {date_specifique}")
print(f"Année : {date_specifique.year}, Mois : {date_specifique.month}, Jour : {date_specifique.day}")
print(f"Jour de la semaine (0-6) : {date_specifique.weekday()}")
print(f"Jour de la semaine ISO (1-7) : {date_specifique.isoweekday()}")
print(f"Jour de l'année : {date_specifique.timetuple().tm_yday}")

# 2. Objet time
print("\n2. Objet time")
heure_actuelle = datetime.datetime.now().time()  # time est une méthode
print(f"Heure actuelle : {heure_actuelle}")
heure_specifique = datetime.time(14, 30, 45, 123456)  # time est une classe
print(f"Heure spécifique : {heure_specifique}")
print(f"Heure : {heure_specifique.hour}, Minute : {heure_specifique.minute}, Seconde : {heure_specifique.second}, Microseconde : {heure_specifique.microsecond}")

# 3. Objet datetime
print("\n3. Objet datetime")
maintenant = datetime.datetime.now()
print(f"Date et heure actuelles : {maintenant}")
date_heure_specifique = datetime.datetime(2024, 8, 18, 14, 30, 45, 123456)
print(f"Date et heure spécifiques : {date_heure_specifique}")
print(f"Date : {date_heure_specifique.date()}, Heure : {date_heure_specifique.time()}")

# 4. Formatage et parsing
print("\n4. Formatage et parsing")
format_date = "%d/%m/%Y %H:%M:%S"
date_formatee = maintenant.strftime(format_date)
print(f"Date formatée : {date_formatee}")
date_parsee = datetime.datetime.strptime("18/08/2024 14:30:45", format_date)
print(f"Date parsée : {date_parsee}")

# 5. Objet timedelta
print("\n5. Objet timedelta")
delta = datetime.timedelta(days=7, hours=3, minutes=15)
future_date = maintenant + delta
print(f"Date dans 7 jours, 3 heures et 15 minutes : {future_date}")
difference = future_date - maintenant
print(f"Différence : {difference}")
print(f"Jours : {difference.days}, Secondes : {difference.seconds}")


# 6. Comparaisons
print("\n6. Comparaisons")
date1 = datetime.datetime(2024, 8, 18)
date2 = datetime.datetime(2024, 8, 19)
print(f"date1 < date2 : {date1 < date2}")
print(f"date1 == date2 : {date1 == date2}")
print(f"date1 != date2 : {date1 != date2}")

# 7. Temps Universel Coordonné (UTC)
print("\n7. UTC")
utc_now = datetime.datetime.now(datetime.timezone.utc)
print(utc_now)
