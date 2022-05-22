# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 7b Activity 2b
# Date:         14 October 2021
#

# Inputs
values = input("Enter three or more values separated by spaces: ")
separator = input("Enter a two-character separator: ")

# add leaning and trailing whitespace
separator = " " + separator + " "

# Print coolness
print(separator.join(values.split(" ")))
