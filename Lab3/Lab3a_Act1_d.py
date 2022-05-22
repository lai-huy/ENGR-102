# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
#               BRANDON A WHITE     331004571
#               WILLIAM A ROBERTS   530008478
#               JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 3a Activity 1d
# Date:         14 SEPTEMBER 2021
#

# Watts input
watts = float(input("Please enter the number of watts to be converted to BTU per hour: "))

# British Thermal Units per hour output
BTU_hr = watts * 3.412141633
print("{:.2f} watts is equivalent to {:.2f} BTU per hour".format(watts, BTU_hr))