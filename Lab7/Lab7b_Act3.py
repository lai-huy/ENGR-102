# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 7b Activity 3
# Date:         14 October 2021
#

from math import *

# Input
A = input("Enter the elements for vector A: ")
B = input("Enter the elements for vector B: ")

# Convert to list
A = [float(c) for c in A.split(" ")]
B = [float(c) for c in B.split(" ")]

# Magnitude calculation
mag_A = sqrt(sum([c ** 2 for c in A]))
mag_B = sqrt(sum([c ** 2 for c in B]))

# sum of vectors
total = [A[i] + B[i] for i in range(len(A))]

# difference of vectors
diff = [A[i] - B[i] for i in range(len(A))]

# partial dot product of vectors
dot = [A[i] * B[i] for i in range(len(A))]

# print epic math
print("The magnitude of vector A is {:.4f}".format(mag_A))
print("The magnitude of vector B is {:.4f}".format(mag_B))
print("A + B is {:s}".format(str(total)))
print("A - B is {:s}".format(str(diff)))
print("The dot product is {:}".format(sum(dot)))
