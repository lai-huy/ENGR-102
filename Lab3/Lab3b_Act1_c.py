# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         HUY Q LAI           132000359
# Section:      ENGR-102-569
# Assignment:   Lab 3b Activity 1c
# Date:         14 SEPTEMBER 2021
#

print("This program calculates how much Radon-222 is left given time and initial amount")
t       = float(input("Please enter the time (days): "))        # Amount of time has passed (days)
N0      = float(input("Please enter the initial amount (g): ")) # Initial amount (g)
t_half  = 3.8   # Half-life (days)
print("Radon-222 left is {:.2f} g".format(N0 * 2 ** (-t/t_half)))
