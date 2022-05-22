# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 4b Activity 4
# Date:         23 SEPTEMBER 2021
#

from math import sqrt

# Input
a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))

# Constants
one_root = "The root is x = {}"
two_root = "The roots are x = {} and x = {}"
i = "i"

# Check Invalid Inputs
if a == 0:
    if b == 0:
        print("You entered an invalid combination of coefficients")
        exit(0)
    print(one_root.format(-c/b))
    exit(0)

# Discriminant
disc = (b**2) - (4 * a * c)

# Real Roots
if disc >= 0:
    pos = (-b + sqrt(disc)) / (2 * a)
    neg = (-b - sqrt(disc)) / (2 * a)

    # One root
    if disc == 0:
        print(one_root.format(pos))

    # Two roots
    else:
        print(two_root.format(pos, neg))

# Complex Roots
else:
    # Fix discriminant
    disc *= -1

    # Real and Complex parts
    real = -b/(2 * a)
    imag = sqrt(disc)/(2 * a)

    pos = "{} + {}{:s}".format(real, imag, i)
    neg = "{} - {}{:s}".format(real, imag, i)
    print(two_root.format(pos, neg))
