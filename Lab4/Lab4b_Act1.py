# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 4b Activity 1
# Date:         23 SEPTEMBER 2021
#

# Input three numbers
x = float(input("Enter number 1: "))
y = float(input("Enter number 2: "))
z = float(input("Enter number 3: "))

# find min
minimum = x
if minimum >= y:
    minimum = y
if minimum >= z:
    minimum = z
print("The smallest number is {}".format(minimum))
