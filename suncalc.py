from astral import LocationInfo
import datetime
from astral.sun import sun

current_latitude = 42.9547653619083
current_longitude = -85.68138301630442

city = LocationInfo("Grand Rapids", "USA", "Eastern", current_latitude, current_longitude)
print((
    f"Information for {city.name}/{city.region}\n"
    f"Timezone: {city.timezone}\n"
    f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
))

s = sun(city.observer, date=datetime.date(2009, 4, 22))

print((
    f'Dawn:    {s["dawn"]}\n'
    f'Sunrise: {s["sunrise"]}\n'
    f'Noon:    {s["noon"]}\n'
    f'Sunset:  {s["sunset"]}\n'
    f'Dusk:    {s["dusk"]}\n'
))
