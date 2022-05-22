# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 3b Activity 2
# Date:         14 SEPTEMBER 2021
#

from math import *


# Find the radius of a circle given area
def circle(area):
    return sqrt(area / pi)


# Find the side length of a regular polygon given area and number of sides.
def reg_poly(area, n):
    return sqrt(4 * a * tan(pi / n) / n)


# inputted area
a = float(input("Please enter the area: "))
print("A circle with area {:.2f} has a radius {:.3f}".format(a, circle(a)))
print("An equilateral triangle with area {:.2f} has a side {:.3f}".format(a, reg_poly(a, 3)))
print("A square with area {:.2f} has a side {:.3f}".format(a, reg_poly(a, 4)))
print("A pentagon with area {:.2f} has a side {:.3f}".format(a, reg_poly(a, 5)))
print("A dodecagon with area {:.2f} has a side {:.3f}".format(a, reg_poly(a, 12)))
