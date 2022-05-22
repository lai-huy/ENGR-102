# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 3b Challenge
# Date:         14 SEPTEMBER 2021
#

from math import pi

# Number of digits to print
digits = int(input("Please enter the number of digits of precision for pi: "))

# {:.#f}
rounded = "{:." + str(digits) + "f}"
print(("The value of pi to {} digits is: " + rounded).format(digits, pi))
