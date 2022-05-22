# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
#               BRANDON A WHITE     331004571
#               WILLIAM A ROBERTS   530008478
#               JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 6a Activity 1b
# Date:         04 October 2021
#

# WHY WOULD YOU NOT USE A LOOP
# :(

n = float(input("Enter the side length in meters: "))
layer = int(input("Enter the number of layers: "))
out = "You need {:.2f} square meters of gold foil to cover the pyramid"

# Sick math
area = (3 * layer ** 2 + 2 * layer) * n ** 2
print(out.format(area))
