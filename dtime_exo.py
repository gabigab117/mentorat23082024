import datetime

date = datetime.datetime(2024, 7, 14, 16, 30, 45)

# 1.1 Formatez la date pour afficher : "14 juillet 2024"
resultat_1 = date.strftime("")
print(resultat_1)

# 1.2 Formatez la date pour afficher : "16h30 - 14/07/2024"
resultat_2 = date.strftime("")
print(resultat_2)

# 1.3 Formatez la date pour afficher : "Dimanche 14 juillet 2024, 16:30:45"
resultat_3 = date.strftime("")
print(resultat_3)


# 2.1 Convertissez la chaîne "21/09/2023 15:45" en objet datetime
date_str_1 = "21/09/2023 15:45"
date_1 = datetime.datetime.strptime(___, ___)
print(date_1)

# 2.2 Convertissez la chaîne "2023-11-30T08:30:00" en objet datetime
date_str_2 = "2023-11-30T08:30:00"
date_2 = datetime.datetime.strptime(___, ___)
print(date_2)

# 2.3 Convertissez la chaîne "15 août 2024 - 09h25" en objet datetime
date_str_3 = "15 août 2024 - 09h25"
date_3 = datetime.datetime.strptime(___, ___)
print(date_3)


date_depart = datetime.datetime(2024, 8, 1, 10, 0)

# 3.1 Calculez la date et l'heure 72 heures après le départ
arrivee_1 = ___
print(f"Arrivée 1 : {arrivee_1}")

# 3.2 Calculez la date et l'heure 10 jours et 12 heures avant le départ
depart_anticipe = ___
print(f"Départ anticipé : {depart_anticipe}")

# 3.3 Ajoutez 3 semaines et 2 jours à la date de départ
nouvelle_date = ___
print(f"Nouvelle date : {nouvelle_date}")


date = datetime.datetime(2024, 2, 29, 15, 30)

# 4.1 Extrayez et affichez le numéro du jour de la semaine (0-6)
jour_semaine = ___
print(f"Jour de la semaine : {jour_semaine}")

# 4.2 Calculez et affichez le numéro de la semaine dans l'année
numero_semaine = ___
print(f"Numéro de la semaine : {numero_semaine}")
