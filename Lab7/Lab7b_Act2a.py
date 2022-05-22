# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 7b Activity 2a
# Date:         14 October 2021
#

# Input
prices = input("Enter three or more prices separated by spaces: ")

# Split into list
prices = prices.split(" ")

# print with format
for price in prices:
    print("${:s}".format(price.rjust(7, " ")))
