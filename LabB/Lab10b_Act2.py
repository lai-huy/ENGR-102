# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 10b Activity 2
# Date:         11 November 2021
#

from matplotlib import pyplot as plt
import numpy as np

reader = open("CLLWeatherData.csv", "r")
lines = reader.readlines()
del lines[0]

# Separate Data into different lists
dates = []
date = []
wind = []
prep = []
temp_ave = []
temp_max = []
temp_min = []

for i in range(len(lines)):
    spt = lines[i].strip().split(",")
    line = [float(i) for i in spt[1:]]
    dates.append([int(i) for i in spt[0].split("/")])
    date.append(i)
    wind.append(line[0])
    prep.append(line[1])
    temp_ave.append(line[2])
    temp_max.append(line[3])
    temp_min.append(line[4])

# Graph Time
fig, ax1 = plt.subplots()

line0, = ax1.plot(date, wind, color="blue")
ax1.set_xlabel("Date")
ax1.set_ylabel("Average Wind Speed (mph)")

ax2 = ax1.twinx()
line1, = ax2.plot(date, temp_ave, color="red")
ax2.set_ylabel("Average Temperature (F)")
ax2.set_title("Average Temperature and Wind Speed")

plt.legend([line0, line1], ["Wind Speed", "Average Temperature"], loc="lower left")
fig.tight_layout()

plt.show()

# Histogram of Precipitation
fig, ax2 = plt.subplots(tight_layout=True)

for i in range(len(prep) - 1, -1, -1):
    if prep[i] == 0.0:
        del prep[i]

Q1 = np.quantile(prep, 0.25)
Q3 = np.quantile(prep, 0.75)
bin_width = 2 * (Q3 - Q1) * len(prep) ** (-1/3)
n_bins = (max(prep) - min(prep))/bin_width

ax2.hist(prep, bins=int(n_bins))
ax2.set_title("Histogram of Precipitation")
ax2.set_xlabel("Precipitation (in)")
ax2.set_ylabel("Number of Days")

plt.show()

# Average Wind Speed vs Minimum Temperature
fig, ax3 = plt.subplots(tight_layout=True)

ax3.scatter(temp_min, wind, color="black", marker=".")
ax3.set_title("Average Wind Speed vs Minimum Temperature")
ax3.set_xlabel("Minimum Temperature (F)")
ax3.set_ylabel("Average Wind Speed (mph)")

plt.show()

# Average Temperature by Month
ave_temp = [[], [], [], [], [], [], [], [], [], [], [], []]
max_temp = [[], [], [], [], [], [], [], [], [], [], [], []]
min_temp = [[], [], [], [], [], [], [], [], [], [], [], []]

MONTH = np.arange(1, 13)

for i in range(len(temp_ave)):
    ave_temp[dates[i][0] - 1].append(temp_ave[i])
    max_temp[dates[i][0] - 1].append(temp_max[i])
    min_temp[dates[i][0] - 1].append(temp_max[i])

for i in range(len(ave_temp)):
    ave_temp[i] = sum(ave_temp[i])/ len(ave_temp[i])
    max_temp[i] = max(max_temp[i])
    min_temp[i] = min(min_temp[i])

fig, ax4 = plt.subplots(tight_layout=True)

ax4.bar(MONTH, ave_temp, color="yellow")
ax4.plot(MONTH, min_temp, color="blue")
ax4.plot(MONTH, max_temp, color="red")

ax4.set_xticks(np.arange(0, 13, 1))
ax4.set_xlabel("Month")
ax4.set_ylabel("Average Temperature (F)")
ax4.set_title("Average Temperature by Month")

plt.show()
