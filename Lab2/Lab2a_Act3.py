# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
#               BRANDON A WHITE     331004571
#               WILLIAM A ROBERTS   530008478
#               JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 2a Activity 3
# Date:         06 SEPTEMBER 2021
#

import math

# Given Data
t1 = 10
t2 = 55
m1 = 2025
m2 = 23025

# Velocity of the ISS
vel = (m2 - m1) / (t2 - t1)

# Part 1
t = 25.0
p = m1 + vel * (t - t1)

print("Part 1:")
print("For t = {} minutes, the position p = {} kilometers".format(t, p))

# Part 2
t = 5.0
cir_earth = 6745 * 2 * math.pi
p = m1 + vel * (t * 60 - t1) % cir_earth

print("Part 2:")
print("For t = {} hours, the position p = {} kilometers".format(t, p))
