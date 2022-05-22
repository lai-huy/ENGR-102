# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 3b Activity 1b
# Date:         14 SEPTEMBER 2021
#

import math

print("This program calculates the wavelength given distance and angle")
d       = float(input("Please enter the distance (nm): "))                          # distance (nm)
theta   = int(input("Please enter the angle (degrees): ")) * math.pi/180    # angle (rad)
print("Wavelength is {:.4f} nm".format(2 * d * math.sin(theta)))
