# Mémo Python: Codes de formatage datetime

| Code | Exemple | Description |
|------|---------|-------------|
| `%a` | `Dim` | Nom abrégé du jour de la semaine |
| `%A` | `Dimanche` | Nom complet du jour de la semaine |
| `%w` | `0` | Jour de la semaine en tant que nombre décimal (0-6, 0 étant Dimanche) |
| `%d` | `18` | Jour du mois (01-31) |
| `%b` | `Août` | Nom abrégé du mois |
| `%B` | `Août` | Nom complet du mois |
| `%m` | `08` | Mois sous forme de nombre (01-12) |
| `%y` | `24` | Année sans siècle (00-99) |
| `%Y` | `2024` | Année avec siècle |
| `%H` | `14` | Heure (format 24 heures, 00-23) |
| `%I` | `02` | Heure (format 12 heures, 01-12) |
| `%p` | `PM` | Indicateur AM ou PM |
| `%M` | `30` | Minute (00-59) |
| `%S` | `45` | Seconde (00-59) |
| `%f` | `000000` | Microsecondes (000000-999999) |
| `%z` | `+0100` | Décalage UTC (±HHMM) |
| `%Z` | `CET` | Nom de fuseau horaire |
| `%j` | `230` | Jour de l'année (001-366) |
| `%U` | `33` | Numéro de semaine de l'année (00-53, Dimanche comme premier jour) |
| `%W` | `33` | Numéro de semaine de l'année (00-53, Lundi comme premier jour) |
| `%c` | `Dim 18 Août 2024 14:30:45` | Représentation de date et heure locale |
| `%x` | `18/08/2024` | Représentation de date locale |
| `%X` | `14:30:45` | Représentation d'heure locale |

Note : Les exemples sont basés sur la date hypothétique du 18 août 2024, 14:30:45.
