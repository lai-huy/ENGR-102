# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 4b Activity 3
# Date:         23 SEPTEMBER 2021
#

# Input
days = int(input("Please enter a positive value for day: "))
days_org = days

# Output
widget = 3820

# Error checking
if days < 0:
    print("You entered an invalid number!")
    exit(0)

# Calculations
if days < 11:
    widget = 10 * days
elif days < 51:
    widget = (days ** 2)/2 + days/2 + 45
elif days < 101:
    widget = 50 * days - 1180
print("The total number of widgets produced on day {:d} is {:d}".format(days_org, int(widget)))
