# suncalc.py generates a CSV file for annual sunrise and sundown data
# using the "astral" Python package found here: https://astral.readthedocs.io/en/latest/index.html#

from astral import LocationInfo
import datetime
from astral.sun import sun

current_year = int(input("What year's sun data are you looking for? "))
current_latitude = float(input("What is your location's latitude, as a unitless decimal value? "))
current_longitude = float(input("What is your location's longitude, as a unitless decimal value?" ))

city = LocationInfo("Grand Rapids", "USA", "Eastern", current_latitude, current_longitude)

# Template code from astral docs
#
# print((
#     f"Information for {city.name}/{city.region}\n"
#     f"Timezone: {city.timezone}\n"
#     f"Latitude: {city.latitude:.02f}; Longitude: {city.longitude:.02f}\n"
# ))

s = sun(city.observer, date=datetime.date(2009, 4, 22))

# Template code from astral docs
#
# print((
#     f'Dawn:    {s["dawn"]}\n'
#     f'Sunrise: {s["sunrise"]}\n'
#     f'Noon:    {s["noon"]}\n'
#     f'Sunset:  {s["sunset"]}\n'
#     f'Dusk:    {s["dusk"]}\n'
# ))

sunrise_list = []
sunset_list = []
date_list = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]


for j in range(0,11):
    for i in range(1, date_list[1][j] + 1):
        query_month = date_list[0][j]
        query_day = i
        # query_date = str(current_year) + "," + str(date_list[0][j]) + "," + str(i)
        s = sun(city.observer, date=datetime.date(current_year, query_month, query_day))
        sunrise_list.append(f'{s["sunrise"]}')
        sunset_list.append(f'{s["sunset"]}')

print(sunrise_list)
print(sunset_list)

# Saves a .csv file to Desktop\User\Aggredicus
## Currently doesn't actually separate out into rows

import csv

# field names
fields = ['Sunrise', 'Sunset']

# data rows of csv file
rows = [ [sunrise_list],
         [sunset_list] ]

# name of csv file
filename = f"{current_year}_suntimes.csv"

# writing to csv file
with open(filename, 'w', newline='') as csvfile:
    # creating a csv writer object
    writer = csv.writer(csvfile)

    # writing the fields
    writer.writerow(fields)

    # writing the data rows
    writer.writerow(rows)

print("File saved to User folder as " + filename)
