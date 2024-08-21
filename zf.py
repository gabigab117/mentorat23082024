import datetime
from zoneinfo import ZoneInfo


los_angles = datetime.datetime.now(tz=ZoneInfo("America/Los_Angeles"))
paris = datetime.datetime.now(tz=ZoneInfo("Europe/Paris"))
print(paris)
print(los_angles)

# Changement de fuseau
seoul = paris.astimezone(ZoneInfo("Asia/Seoul"))
print(seoul)

# https://data.iana.org/time-zones/tzdb-2021a/zone1970.tab

