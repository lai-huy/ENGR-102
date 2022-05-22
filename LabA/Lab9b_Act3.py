# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 9b Activity 3
# Date:         04 November 2021
#

import csv

KEYS = ["Date", "Average Daily Wind Speed (mph)", "Precipitation (in)", "Average Temperature (F)",
        "Maximum Temperature (F)", "Minimum Temperature (F)"]
DAYS = {"January": [0, 31],
        "February": [1, 28],
        "March": [2, 31],
        "April": [3, 30],
        "May": [4, 31],
        "June": [5, 30],
        "July": [6, 31],
        "August": [7, 31],
        "September": [8, 30],
        "October": [9, 31],
        "November": [10, 30],
        "December": [11, 31]}
DAYS_LEAP = {"January": [0, 31],
             "February": [1, 29],
             "March": [2, 31],
             "April": [3, 30],
             "May": [4, 31],
             "June": [5, 30],
             "July": [6, 31],
             "August": [7, 31],
             "September": [8, 30],
             "October": [9, 31],
             "November": [10, 30],
             "December": [11, 31]}

reader = open("CLLWeatherData.csv", "r")

data_dict = csv.DictReader(reader)

# Holds raw data
data = []

# Split data
wind = []
prep = []
temperature = []
max_temp = []
min_temp = []

for line in data_dict:
    data.append(list(line.values()))
    wind.append(float(line[KEYS[1]]))
    prep.append(float(line[KEYS[2]]))
    temperature.append(float(line[KEYS[3]]))
    max_temp.append(float(line[KEYS[4]]))
    min_temp.append(float(line[KEYS[5]]))

print(f"3-year maximum temperature: {max(max_temp):.0f} F")
print(f"3-year minimum temperature: {min(min_temp):.0f} F")
print(f"3-year average precipitation: {sum(prep) / len(prep):.3f} inches")

print()
month = input("Please enter a month: ")
year = int(input("Please enter a year: "))
print()

# Access correct Data
index = 365 * year - 736570
days = DAYS_LEAP if not year % 4 else DAYS
for i in range(days[month][0]):
    index += days[list(days.keys())[i]][1]

# Split data
wind = []
prep = []
temperature = []
end = index + days[month][1]

for i in range(index, end):
    line = data[i]
    wind.append(float(line[1]))
    prep.append(float(line[2]))
    temperature.append(float(line[3]))

mean_temp = sum(temperature) / len(temperature)
wind_10 = []

for i in wind:
    if i > 10:
        wind_10.append(i)

mean_ws = len(wind_10) / len(wind) * 100
mean_dp = sum(prep) / len(prep)

print(f"For {month} {year}:")
print(f"Mean daily temperature: {mean_temp:.1f} F")
print(f"Percentage of days with average wind speed above 10 mph: {mean_ws:.1f}%")
print(f"Mean daily precipitation: {mean_dp:.4f} inches")
