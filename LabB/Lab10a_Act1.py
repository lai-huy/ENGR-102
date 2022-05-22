# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: HUY Q LAI           132000359
#       BRANDON A WHITE     331004571
#       WILLIAM A ROBERTS   530008478
#       JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 10a Activity 1
# Date:         09 November 2021
#
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import numpy as np

# Matrix Creation
A = np.zeros((3, 4)).astype(int)
B = np.zeros((4, 2)).astype(int)
C = np.zeros((2, 3)).astype(int)

for i in range(A.size):
    A[i // (A.shape[0] + 1)][i % A.shape[1]] = int(i)

for i in range(B.size):
    B[int(i/2)][i % B.shape[1]] = int(i)

for i in range(C.size):
    C[i // (C.shape[0] + 1)][i % C.shape[1]] = int(i)

# Print Matrix
print(f"A = {A}", end="\n\n")
print(f"B = {B}", end="\n\n")
print(f"C = {C}", end="\n\n")

# Multiply Matrix and find its transposition
D = np.matmul(np.matmul(A, B), C)
print(f"D = {D}", end="\n\n")
print(f"D^T = {D.transpose()}", end="\n\n")

# E
E = np.sqrt(D)/2
print(f"E = {E}")
