import datetime
from zoneinfo import ZoneInfo

# Depuis Python 3.9


los_angeles = datetime.datetime.now(tz=ZoneInfo("America/Los_Angeles"))
paris = datetime.datetime.now(tz=ZoneInfo("Europe/Paris"))
print(paris)
print(los_angeles)

# Changement de fuseau
seoul = paris.astimezone(ZoneInfo("Asia/Seoul"))
print(seoul)

# https://data.iana.org/time-zones/tzdb-2021a/zone1970.tab

