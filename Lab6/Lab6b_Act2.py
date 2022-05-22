# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 6b Activity 2
# Date:         06 October 2021
#

# Constants
sum_out = "The sum of all integers from 0 to {:d} is {:d}"
prod_out = "The product of all integers from 1 to {:d} is {:d}"

# input
n = int(input("Enter an integer: "))
total = 0
prod = 1

# Sum
for i in range(n + 1):
    total += i

# Product
for i in range(2, n + 1):
    prod *= i

# Prints
print(sum_out.format(n, total))
print(prod_out.format(n, prod))
