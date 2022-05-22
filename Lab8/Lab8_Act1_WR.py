# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name: HUY Q LAI           132000359
#       BRANDON A WHITE     331004571
#       WILLIAM A ROBERTS   530008478
#       JOHN RIOS JR        631004090
# Section:      ENGR-102-569
# Assignment:   Lab 8 Activity 1 Final
# Date:         19 October 2021
#

T_scaled = 0
data = []

# Get all necessary data
val = data[T_scaled]

# Next row values
val_next = data[T_scaled + 1]

# Calculate Slope for volume
slope = [(i - j) / 20 for i, j in zip(val_next, val)]